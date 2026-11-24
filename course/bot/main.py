import asyncio
import io
import logging
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    BufferedInputFile,
)

from config import BOT_TOKEN, DATA_PATH
from services.prediction_service import PredictionService
from services.olap_service import OLAPService, DIMENSIONS, MEASURES, AGGS
from services.data_service import DataService


logging.basicConfig(level=logging.INFO)
router = Router()

pred_service = PredictionService()
olap_service = OLAPService()
df_dataset = DataService.load_csv(str(DATA_PATH)) if DATA_PATH.exists() else None


class PredictForm(StatesGroup):
    model = State()
    time_on_site = State()
    age = State()
    income = State()
    internet = State()
    gender = State()
    month = State()
    dow = State()
    hour = State()


class OLAPForm(StatesGroup):
    rows = State()
    cols = State()
    measure = State()
    agg = State()
    gender = State()



def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Предсказать клик"), KeyboardButton(text="Построить OLAP-куб")],
            [KeyboardButton(text="Графики"), KeyboardButton(text="Метрики моделей")],
            [KeyboardButton(text="История (БД)")],
        ],
        resize_keyboard=True,
    )



@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "<b>Система анализа и прогнозирования отклика на рекламу</b>\n\n"
        "Бот подключён к общему ML-ядру и базе данных <code>SQLite3</code> десктоп-приложения.\n"
        "Выберите действие в меню ниже:",
        parse_mode="HTML",
        reply_markup=main_menu(),
    )


@router.message(Command("metrics"))
@router.message(F.text == "Метрики моделей")
async def show_metrics(message: Message):
    metrics = pred_service.predictor.metrics
    if not metrics:
        await message.answer("Метрики не найдены. Проверьте папку models/.")
        return

    lines = ["<b>Качество обученных моделей (тестовая выборка):</b>\n"]
    for m in metrics.values():
        lines.append(
            f"- <b>{m['name']}</b>\n"
            f"  Accuracy: <code>{m['accuracy']:.3f}</code> | "
            f"F1: <code>{m['f1']:.3f}</code> | "
            f"ROC-AUC: <code>{m['roc_auc']:.3f}</code>"
        )
    await message.answer("\n".join(lines), parse_mode="HTML")


@router.message(Command("olap"))
@router.message(F.text == "Построить OLAP-куб")
async def start_olap(message: Message, state: FSMContext):
    if df_dataset is None:
        await message.answer("Файл advertising.csv не найден.")
        return

    dims = list(DIMENSIONS.keys())
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=d, callback_data=f"olap_r:{i}")] for i, d in enumerate(dims)]
    )
    await state.set_state(OLAPForm.rows)
    await message.answer("1/5. Выберите измерение для <b>строк куба</b>:", parse_mode="HTML", reply_markup=kb)


@router.callback_query(OLAPForm.rows, F.data.startswith("olap_r:"))
async def process_olap_rows(callback: CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    row_dim = list(DIMENSIONS.keys())[idx]
    await state.update_data(row_dim=row_dim)

    cols_options = ["Без столбцов (1D)"] + list(DIMENSIONS.keys())
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=c, callback_data=f"olap_c:{i}")] for i, c in enumerate(cols_options)]
    )
    await state.set_state(OLAPForm.cols)
    await callback.message.answer("2/5. Выберите измерение для <b>столбцов куба</b>:", parse_mode="HTML", reply_markup=kb)
    await callback.answer()


@router.callback_query(OLAPForm.cols, F.data.startswith("olap_c:"))
async def process_olap_cols(callback: CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    cols_options = ["Без столбцов (1D)"] + list(DIMENSIONS.keys())
    await state.update_data(col_dim=cols_options[idx])

    measures = list(MEASURES.keys())
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=m, callback_data=f"olap_m:{i}")] for i, m in enumerate(measures)]
    )
    await state.set_state(OLAPForm.measure)
    await callback.message.answer("3/5. Выберите <b>анализируемую меру</b>:", parse_mode="HTML", reply_markup=kb)
    await callback.answer()


@router.callback_query(OLAPForm.measure, F.data.startswith("olap_m:"))
async def process_olap_measure(callback: CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    measure = list(MEASURES.keys())[idx]
    await state.update_data(measure=measure)

    aggs = list(AGGS.keys())
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=a, callback_data=f"olap_a:{i}")] for i, a in enumerate(aggs)]
    )
    await state.set_state(OLAPForm.agg)
    await callback.message.answer("4/5. Выберите <b>функцию агрегации</b>:", parse_mode="HTML", reply_markup=kb)
    await callback.answer()


@router.callback_query(OLAPForm.agg, F.data.startswith("olap_a:"))
async def process_olap_agg(callback: CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    agg = list(AGGS.keys())[idx]
    await state.update_data(agg=agg)

    genders = ["Все", "Только женщины (0)", "Только мужчины (1)"]
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=g, callback_data=f"olap_g:{i}")] for i, g in enumerate(genders)]
    )
    await state.set_state(OLAPForm.gender)
    await callback.message.answer("5/5. Выберите <b>фильтр по полу</b>:", parse_mode="HTML", reply_markup=kb)
    await callback.answer()


@router.callback_query(OLAPForm.gender, F.data.startswith("olap_g:"))
async def finish_olap(callback: CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    genders = ["Все", "Только женщины (0)", "Только мужчины (1)"]
    gender = genders[idx]

    data = await state.get_data()
    await state.clear()

    pivot, summary = olap_service.build_cube(
        df_dataset, data["row_dim"], data["col_dim"], data["measure"], data["agg"], gender
    )
    table_str = pivot.head(15).to_string(index=False)

    await callback.message.answer(
        f"<b>Многомерный OLAP-срез</b>\n{summary}\n\n<pre>{table_str}</pre>",
        parse_mode="HTML",
    )

    # Строим и отправляем тепловую карту (или столбчатый график для 1D)
    fig, ax = plt.subplots(figsize=(7, 5))
    numeric_df = pivot.set_index(pivot.columns[0]).select_dtypes(include=[np.number])

    if not numeric_df.empty:
        if numeric_df.shape[1] > 1:
            im = ax.imshow(numeric_df.values, cmap="YlGnBu", aspect="auto")
            ax.set_xticks(range(len(numeric_df.columns)))
            ax.set_xticklabels([str(c) for c in numeric_df.columns], rotation=30)
            ax.set_yticks(range(len(numeric_df.index)))
            ax.set_yticklabels([str(i) for i in numeric_df.index])
            for i in range(numeric_df.shape[0]):
                for j in range(numeric_df.shape[1]):
                    ax.text(j, i, f"{numeric_df.values[i, j]:.2f}", ha="center", va="center", color="black")
            fig.colorbar(im, ax=ax)
            ax.set_title(f"Тепловая карта OLAP: {data['row_dim']} × {data['col_dim']}")
        else:
            numeric_df.iloc[:, 0].plot(kind="bar", ax=ax, color="#2b5b84")
            ax.set_title(f"OLAP-срез: {data['row_dim']}")
            ax.grid(axis="y", linestyle="--", alpha=0.5)

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=130)
        plt.close(fig)

        photo = BufferedInputFile(buf.getvalue(), filename="olap_heatmap.png")
        await callback.message.answer_photo(photo, caption="Визуализация построенного OLAP-куба", reply_markup=main_menu())

    await callback.answer()


@router.message(Command("charts"))
@router.message(F.text == "Графики")
async def send_metrics_chart(message: Message):
    metrics = pred_service.predictor.metrics
    if not metrics:
        await message.answer("Метрики не найдены.")
        return

    names = [m["name"] for m in metrics.values()]
    acc = [m["accuracy"] for m in metrics.values()]
    f1 = [m["f1"] for m in metrics.values()]
    auc = [m["roc_auc"] for m in metrics.values()]

    x = np.arange(len(names))
    width = 0.25

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(x - width, acc, width, label="Accuracy", color="#2b5b84")
    ax.bar(x, f1, width, label="F1-score", color="#4a90e2")
    ax.bar(x + width, auc, width, label="ROC-AUC", color="#50b89e")

    ax.set_ylabel("Значение метрики")
    ax.set_title("Сравнение качества моделей (LR, DT, MLP)")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=10)
    ax.set_ylim(0, 1.1)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=130)
    plt.close(fig)

    photo = BufferedInputFile(buf.getvalue(), filename="metrics_chart.png")
    await message.answer_photo(photo, caption="Сравнительная диаграмма метрик обученных моделей")



@router.message(Command("history"))
@router.message(F.text == "История (БД)")
async def show_history(message: Message):
    records = pred_service.db.get_records("Все")[:5]
    if not records:
        await message.answer("История действий пока пуста.")
        return

    lines = ["<b>Последние 5 действий из общей БД:</b>\n"]
    for rec in records:
        rec_id, dt, src, model_name, _, prob, pred_txt = rec
        lines.append(
            f"#{rec_id} [{src}] {dt}\n"
            f"Модель: {model_name} -> <b>{pred_txt}</b> ({prob * 100:.1f}%)\n"
        )
    await message.answer("\n".join(lines), parse_mode="HTML")


@router.message(Command("predict"))
@router.message(F.text == "Предсказать клик")
async def start_predict(message: Message, state: FSMContext):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Логистическая регрессия (LR)", callback_data="model:lr")],
            [InlineKeyboardButton(text="Дерево решений (DT)", callback_data="model:dt")],
            [InlineKeyboardButton(text="Нейросеть (MLP)", callback_data="model:mlp")],
        ]
    )
    await state.set_state(PredictForm.model)
    await message.answer("1/9. Выберите модель машинного обучения:", reply_markup=kb)


@router.callback_query(PredictForm.model, F.data.startswith("model:"))
async def process_model(callback: CallbackQuery, state: FSMContext):
    model_key = callback.data.split(":")[1]
    await state.update_data(model_key=model_key)
    await state.set_state(PredictForm.time_on_site)
    await callback.message.answer(
        "2/9. Введите <b>время на сайте в день</b> (в минутах, например <code>68.95</code>):",
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(PredictForm.time_on_site)
async def process_time(message: Message, state: FSMContext):
    try:
        val = float(message.text.replace(",", "."))
        if not 0.0 <= val <= 200.0:
            raise ValueError
        await state.update_data(time_on_site=val)
        await state.set_state(PredictForm.age)
        await message.answer(
            "3/9. Введите <b>возраст</b> пользователя (от <code>18</code> до <code>100</code>, например <code>35</code>):",
            parse_mode="HTML",
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите число от 0 до 200 минут (например, 65.5).")


@router.message(PredictForm.age)
async def process_age(message: Message, state: FSMContext):
    try:
        val = int(message.text)
        if not 18 <= val <= 100:
            raise ValueError
        await state.update_data(age=val)
        await state.set_state(PredictForm.income)
        await message.answer(
            "4/9. Введите <b>доход региона</b> (от <code>0</code> до <code>250000</code>, например <code>61833.9</code>):",
            parse_mode="HTML",
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите целый возраст от 18 до 100 лет.")


@router.message(PredictForm.income)
async def process_income(message: Message, state: FSMContext):
    try:
        val = float(message.text.replace(",", "."))
        if not 0.0 <= val <= 250000.0:
            raise ValueError
        await state.update_data(income=val)
        await state.set_state(PredictForm.internet)
        await message.answer(
            "5/9. Введите <b>суточный интернет-трафик</b> в МБ (от <code>0</code> до <code>500</code>, например <code>256.09</code>):",
            parse_mode="HTML",
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите доход от 0 до 250000.")


@router.message(PredictForm.internet)
async def process_internet(message: Message, state: FSMContext):
    try:
        val = float(message.text.replace(",", "."))
        if not 0.0 <= val <= 500.0:
            raise ValueError
        await state.update_data(internet=val)
        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Женщина (0)", callback_data="gender:0"),
                    InlineKeyboardButton(text="Мужчина (1)", callback_data="gender:1"),
                ]
            ]
        )
        await state.set_state(PredictForm.gender)
        await message.answer("6/9. Выберите <b>пол</b> пользователя:", parse_mode="HTML", reply_markup=kb)
    except ValueError:
        await message.answer("Ошибка ввода: укажите трафик от 0 до 500 МБ.")



@router.callback_query(PredictForm.gender, F.data.startswith("gender:"))
async def process_gender(callback: CallbackQuery, state: FSMContext):
    val = int(callback.data.split(":")[1])
    await state.update_data(gender=val)
    await state.set_state(PredictForm.month)
    await callback.message.answer(
        "7/9. Введите <b>номер месяца</b> (от <code>1</code> до <code>12</code>):",
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(PredictForm.month)
async def process_month(message: Message, state: FSMContext):
    try:
        val = int(message.text)
        if not 1 <= val <= 12:
            raise ValueError
        await state.update_data(month=val)
        await state.set_state(PredictForm.dow)
        await message.answer(
            "8/9. Введите <b>день недели</b> (<code>0</code> — Пн, ..., <code>6</code> — Вс):",
            parse_mode="HTML",
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите число от 1 до 12.")


@router.message(PredictForm.dow)
async def process_dow(message: Message, state: FSMContext):
    try:
        val = int(message.text)
        if not 0 <= val <= 6:
            raise ValueError
        await state.update_data(dow=val)
        await state.set_state(PredictForm.hour)
        await message.answer(
            "9/9. Введите <b>час дня</b> (от <code>0</code> до <code>23</code>):",
            parse_mode="HTML",
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите число от 0 до 6.")


@router.message(PredictForm.hour)
async def process_hour(message: Message, state: FSMContext):
    try:
        val = int(message.text)
        if not 0 <= val <= 23:
            raise ValueError
        data = await state.get_data()

        user_features = {
            "Daily Time Spent on Site": data["time_on_site"],
            "Age": data["age"],
            "Area Income": data["income"],
            "Daily Internet Usage": data["internet"],
            "Male": data["gender"],
            "Month": data["month"],
            "DayOfWeek": data["dow"],
            "Hour": val,
        }

        res = pred_service.predict_and_save(user_features, model_key=data["model_key"], source="Telegram")
        await state.clear()

        await message.answer(
            f"<b>Результат прогноза:</b> {res['message']}\n"
            f"<b>Вероятность клика:</b> <code>{res['probability'] * 100:.2f}%</code>\n"
            f"<b>Модель:</b> {res['model_name']}\n\n"
            f"<i>Запись сохранена в общую базу SQLite3 и доступна в десктоп-приложении.</i>",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
    except ValueError:
        await message.answer("Ошибка ввода: укажите число от 0 до 23.")

@router.message()
async def handle_unknown_message(message: Message):
    await message.answer(
        "Я не понимаю эту команду. Пожалуйста, выберите действие с помощью кнопок меню ниже:",
        reply_markup=main_menu(),
    )


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в файле .env.")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
