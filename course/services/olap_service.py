import random
import pandas as pd
from services.data_service import DataService

DIMENSIONS = {
    "Месяц (Month)": "Month",
    "День недели (DayOfWeek)": "DayOfWeek",
    "Час (Hour)": "Hour",
    "Пол (Male)": "Male",
    "Возрастная группа (Age_Group)": "Age_Group",
    "Страна (Country)": "Country",
}

MEASURES = {
    "Клик по рекламе (Clicked on Ad)": "Clicked on Ad",
    "Время на сайте (Daily Time Spent on Site)": "Daily Time Spent on Site",
    "Трафик (Daily Internet Usage)": "Daily Internet Usage",
    "Доход региона (Area Income)": "Area Income",
    "Возраст (Age)": "Age",
}

AGGS = {
    "Среднее (mean)": "mean",
    "Количество (count)": "count",
    "Сумма (sum)": "sum",
    "Максимум (max)": "max",
    "Минимум (min)": "min",
}

class OLAPService:
    @staticmethod
    def build_cube(df: pd.DataFrame, row_label: str, col_label: str, measure_label: str, agg_label: str, gender_filter: str = "Все") -> tuple[pd.DataFrame, str]:
        df_prep = DataService.preprocess(df)

        if gender_filter == "Только женщины (0)" and "Male" in df_prep.columns:
            df_prep = df_prep[df_prep["Male"] == 0]
        elif gender_filter == "Только мужчины (1)" and "Male" in df_prep.columns:
            df_prep = df_prep[df_prep["Male"] == 1]

        row_col = DIMENSIONS[row_label]
        measure_col = MEASURES[measure_label]
        agg_func = AGGS[agg_label]

        if col_label == "Без столбцов (1D)" or DIMENSIONS.get(col_label) == row_col:
            pivot = df_prep.groupby(row_col)[measure_col].agg(agg_func).reset_index()
            pivot.columns = [row_label, f"{measure_label} ({agg_func})"]
        else:
            col_col = DIMENSIONS[col_label]
            pivot = pd.pivot_table(
                df_prep, values=measure_col, index=row_col, columns=col_col, aggfunc=agg_func, fill_value=0
            ).reset_index()

        pivot = pivot.round(3)
        summary = f"Срез: {row_label} × {col_label} | Мера: {measure_label} ({agg_func}) | Фильтр пола: {gender_filter} | Строк в выборке: {len(df_prep)}"
        return pivot, summary

    @staticmethod
    def get_random_params() -> tuple[str, str, str, str, str]:
        r = random.choice(list(DIMENSIONS.keys())[:-1])  # без Country, чтобы куб был компактным
        c_choices = ["Без столбцов (1D)"] + [k for k in list(DIMENSIONS.keys())[:-1] if k != r]
        c = random.choice(c_choices)
        m = random.choice(list(MEASURES.keys()))
        a = random.choice(list(AGGS.keys()))
        g = random.choice(["Все", "Только женщины (0)", "Только мужчины (1)"])
        return r, c, m, a, g
