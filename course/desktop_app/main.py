import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pandas as pd
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox,
    QTableWidgetItem, QHeaderView, QVBoxLayout
)
from PySide6.QtCore import Qt, Slot

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.metrics import confusion_matrix

from ui_mainwindow import Ui_MainWindow
from worker import PredictWorker, BatchPredictWorker
from config import DATA_PATH
from services.prediction_service import PredictionService
from services.data_service import DataService
from services.olap_service import OLAPService, DIMENSIONS, MEASURES, AGGS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Система анализа и прогнозирования отклика на рекламу")

        self.pred_service = PredictionService()
        self.data_service = DataService()
        self.olap_service = OLAPService()

        self.df = None
        self.last_olap_df = None
        self.worker = None

        self._init_controls()
        self._init_plot_canvas()
        self._connect_signals()
        self._load_initial_data()

    def _init_controls(self):
        # 1. Вкладка "Предсказания" (3 модели)
        self.model_keys = ["lr", "dt", "mlp"]
        self.ui.combo_model.addItems([
            "Логистическая регрессия (LR)",
            "Дерево решений (DT)",
            "Нейросеть (MLP)"
        ])
        self.ui.combo_gender.addItems(["Женщина (0)", "Мужчина (1)"])

        self.ui.spin_time.setRange(0.0, 200.0)
        self.ui.spin_time.setValue(68.95)
        self.ui.spin_age.setRange(18, 100)
        self.ui.spin_age.setValue(35)
        self.ui.spin_income.setRange(0.0, 250000.0)
        self.ui.spin_income.setValue(61833.90)
        self.ui.spin_internet.setRange(0.0, 500.0)
        self.ui.spin_internet.setValue(256.09)
        self.ui.spin_month.setRange(1, 12)
        self.ui.spin_month.setValue(3)
        self.ui.spin_dow.setRange(0, 6)
        self.ui.spin_dow.setValue(6)
        self.ui.spin_hour.setRange(0, 23)
        self.ui.spin_hour.setValue(10)

        # 2. Вкладка "OLAP"
        self.ui.combo_olap_rows.addItems(list(DIMENSIONS.keys()))
        self.ui.combo_olap_cols.addItems(["Без столбцов (1D)"] + list(DIMENSIONS.keys()))
        self.ui.combo_olap_cols.setCurrentIndex(4)
        self.ui.combo_olap_measure.addItems(list(MEASURES.keys()))
        self.ui.combo_olap_agg.addItems(list(AGGS.keys()))
        self.ui.combo_olap_filter_gender.addItems(["Все", "Только женщины (0)", "Только мужчины (1)"])

        # 3. Вкладка "Результаты"
        self.ui.combo_plot_type.addItems([
            "Сравнение метрик моделей (Bar chart)",
            "Матрица ошибок: Логистическая регрессия",
            "Матрица ошибок: Дерево решений",
            "Матрица ошибок: Нейросеть (MLP)",
            "Тепловая карта текущего OLAP-куба"
        ])

        # 4. Вкладка "История"
        self.ui.combo_history_source.addItems(["Все", "Desktop", "Telegram"])

        self.ui.table_widget.setCurrentIndex(0)
        self._update_selected_model_metrics()
        self._populate_metrics_table()
        self._refresh_history()

    def _init_plot_canvas(self):
        layout = QVBoxLayout(self.ui.widget_plot)
        layout.setContentsMargins(5, 5, 5, 5)
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def _connect_signals(self):
        self.ui.btn_load_csv.clicked.connect(self.on_load_csv)
        self.ui.btn_preprocess.clicked.connect(self.on_preprocess)
        self.ui.btn_batch_predict.clicked.connect(self.on_batch_predict)
        self.ui.btn_export_csv.clicked.connect(self.on_export_csv)

        self.ui.btn_olap_build.clicked.connect(self.on_build_olap)
        self.ui.btn_olap_random.clicked.connect(self.on_random_olap)

        self.ui.combo_model.currentIndexChanged.connect(self._update_selected_model_metrics)
        self.ui.btn_predict.clicked.connect(self.on_predict_clicked)

        self.ui.btn_draw_plot.clicked.connect(self.on_draw_plot)

        self.ui.btn_refresh_history.clicked.connect(self._refresh_history)
        self.ui.combo_history_source.currentIndexChanged.connect(self._refresh_history)
        self.ui.btn_clear_history.clicked.connect(self.on_clear_history)

    def _load_initial_data(self):
        if DATA_PATH.exists():
            self.df = self.data_service.load_csv(str(DATA_PATH))
            self.ui.lbl_data_status.setText(
                f"✅ Автозагрузка: advertising.csv ({self.df.shape[0]} строк, {self.df.shape[1]} столбцов)"
            )
            self._fill_table(self.ui.table_data, self.df.head(100))
            self.on_build_olap()
            self.on_draw_plot()
        else:
            self.ui.lbl_data_status.setText("⚠️ Загрузите файл advertising.csv")

    def _fill_table(self, table_widget, df: pd.DataFrame):
        table_widget.clear()
        table_widget.setRowCount(df.shape[0])
        table_widget.setColumnCount(df.shape[1])
        table_widget.setHorizontalHeaderLabels([str(c) for c in df.columns])

        for r in range(df.shape[0]):
            for c in range(df.shape[1]):
                val = df.iloc[r, c]
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(r, c, item)

        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    @Slot()
    def on_load_csv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть CSV", str(ROOT_DIR), "CSV Files (*.csv)")
        if not path:
            return
        try:
            self.df = self.data_service.load_csv(path)
            self.ui.lbl_data_status.setText(f"✅ Загружен файл: {Path(path).name} ({self.df.shape[0]} строк)")
            self._fill_table(self.ui.table_data, self.df.head(100))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка загрузки", str(e))

    @Slot()
    def on_preprocess(self):
        if self.df is None:
            QMessageBox.warning(self, "Внимание", "Сначала загрузите CSV!")
            return
        try:
            self.df = self.data_service.preprocess(self.df)
            self.ui.lbl_data_status.setText(f"✅ Предобработка завершена ({self.df.shape[1]} признаков)")
            self._fill_table(self.ui.table_data, self.df.head(100))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка предобработки", str(e))

    @Slot()
    def on_batch_predict(self):
        if self.df is None:
            QMessageBox.warning(self, "Внимание", "Сначала загрузите CSV!")
            return
        model_key = self.model_keys[self.ui.combo_model.currentIndex()]
        if model_key not in self.pred_service.predictor.models:
            QMessageBox.critical(self, "Ошибка", "Модели не найдены в папке models/. Запустите ячейку в ноутбуке.")
            return

        pipe = self.pred_service.predictor.models[model_key]["model"]
        self.ui.btn_batch_predict.setEnabled(False)
        self.ui.lbl_data_status.setText("⏳ Выполняется пакетный прогноз...")

        self.worker = BatchPredictWorker(self.data_service, self.df, pipe)
        self.worker.finished_ok.connect(self._on_batch_done)
        self.worker.failed.connect(self._on_batch_error)
        self.worker.start()

    @Slot(object)
    def _on_batch_done(self, res_df):
        self.df = res_df
        self._fill_table(self.ui.table_data, self.df.head(100))
        clicks = int(self.df["Predicted_Click"].sum())
        self.ui.lbl_data_status.setText(f"✅ Прогноз готов! Ожидается кликов: {clicks} из {len(self.df)}")
        self.ui.btn_batch_predict.setEnabled(True)

    @Slot(str)
    def _on_batch_error(self, err):
        self.ui.lbl_data_status.setText(f"❌ Ошибка: {err}")
        self.ui.btn_batch_predict.setEnabled(True)

    @Slot()
    def on_export_csv(self):
        if self.df is None:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить CSV", str(ROOT_DIR / "predictions_output.csv"), "CSV Files (*.csv)")
        if path:
            self.df.to_csv(path, index=False)
            QMessageBox.information(self, "Успех", f"Файл сохранён:\n{path}")

    @Slot()
    def on_build_olap(self):
        if self.df is None:
            QMessageBox.warning(self, "Внимание", "Сначала загрузите данные на вкладке «Данные»!")
            return
        try:
            pivot, summary = self.olap_service.build_cube(
                self.df,
                self.ui.combo_olap_rows.currentText(),
                self.ui.combo_olap_cols.currentText(),
                self.ui.combo_olap_measure.currentText(),
                self.ui.combo_olap_agg.currentText(),
                self.ui.combo_olap_filter_gender.currentText()
            )
            self.last_olap_df = pivot
            self.ui.lbl_olap_summary.setText(summary)
            self._fill_table(self.ui.table_olap, pivot)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка OLAP", str(e))

    @Slot()
    def on_random_olap(self):
        r, c, m, a, g = self.olap_service.get_random_params()
        self.ui.combo_olap_rows.setCurrentText(r)
        self.ui.combo_olap_cols.setCurrentText(c)
        self.ui.combo_olap_measure.setCurrentText(m)
        self.ui.combo_olap_agg.setCurrentText(a)
        self.ui.combo_olap_filter_gender.setCurrentText(g)
        self.on_build_olap()

    @Slot()
    def _update_selected_model_metrics(self):
        key = self.model_keys[self.ui.combo_model.currentIndex()]
        m = self.pred_service.predictor.metrics.get(key)
        if m:
            self.ui.lbl_model_metrics_3.setText(f"Accuracy: {m['accuracy']:.3f} | F1: {m['f1']:.3f}")
        else:
            self.ui.lbl_model_metrics_3.setText("Метрики не загружены")

    @Slot()
    def on_predict_clicked(self):
        user_data = {
            "Daily Time Spent on Site": self.ui.spin_time.value(),
            "Age": self.ui.spin_age.value(),
            "Area Income": self.ui.spin_income.value(),
            "Daily Internet Usage": self.ui.spin_internet.value(),
            "Male": self.ui.combo_gender.currentIndex(),
            "Month": self.ui.spin_month.value(),
            "DayOfWeek": self.ui.spin_dow.value(),
            "Hour": self.ui.spin_hour.value(),
        }
        model_key = self.model_keys[self.ui.combo_model.currentIndex()]

        self.ui.btn_predict.setEnabled(False)
        self.ui.lbl_predict_result.setText("⏳ Вычисление вероятности...")

        self.worker = PredictWorker(self.pred_service, user_data, model_key)
        self.worker.finished_ok.connect(self._on_predict_success)
        self.worker.failed.connect(self._on_predict_error)
        self.worker.start()

    @Slot(dict)
    def _on_predict_success(self, res: dict):
        prob_pct = res["probability"] * 100
        bg_color = "#1f6e43" if res["class"] == 1 else "#2b4c6f"
        self.ui.lbl_predict_result.setStyleSheet(
            f"font-size: 20px; font-weight: bold; color: white; background-color: {bg_color}; border-radius: 8px; padding: 14px;"
        )
        self.ui.lbl_predict_result.setText(
            f"{res['message']}\nВероятность клика: {prob_pct:.2f}%  |  Модель: {res['model_name']}"
        )
        self.ui.btn_predict.setEnabled(True)
        self._refresh_history()

    @Slot(str)
    def _on_predict_error(self, err: str):
        self.ui.lbl_predict_result.setText(f"❌ Ошибка: {err}")
        self.ui.btn_predict.setEnabled(True)

    def _populate_metrics_table(self):
        metrics = self.pred_service.predictor.metrics
        if not metrics:
            return
        rows = []
        for key, m in metrics.items():
            rows.append({
                "Модель": m["name"],
                "Accuracy": m["accuracy"],
                "Precision": m["precision"],
                "Recall": m["recall"],
                "F1-score": m["f1"],
                "ROC-AUC": m["roc_auc"],
            })
        self._fill_table(self.ui.table_metrics_2, pd.DataFrame(rows))

    @Slot()
    def on_draw_plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        idx = self.ui.combo_plot_type.currentIndex()
        metrics = self.pred_service.predictor.metrics

        if idx == 0 and metrics:
            names = [m["name"].split("(")[0].strip() for m in metrics.values()]
            acc = [m["accuracy"] for m in metrics.values()]
            f1 = [m["f1"] for m in metrics.values()]
            x = np.arange(len(names))
            ax.bar(x - 0.18, acc, width=0.35, label="Accuracy", color="#2b5b84")
            ax.bar(x + 0.18, f1, width=0.35, label="F1-score", color="#4ca3dd")
            ax.set_xticks(x)
            ax.set_xticklabels(names, rotation=15, fontsize=9)
            ax.set_ylim(0.8, 1.02)
            ax.set_title("Сравнение качества моделей")
            ax.legend()

        elif idx in (1, 2, 3) and metrics:
            key = ["lr", "dt", "mlp"][idx - 1]
            if key in metrics:
                cm = confusion_matrix(metrics[key]["y_test"], metrics[key]["y_pred"])
                im = ax.imshow(cm, cmap="Blues")
                self.figure.colorbar(im, ax=ax)
                ax.set_xticks([0, 1])
                ax.set_yticks([0, 1])
                ax.set_xticklabels(["Не кликнул (0)", "Кликнул (1)"])
                ax.set_yticklabels(["Не кликнул (0)", "Кликнул (1)"])
                ax.set_xlabel("Предсказание модели")
                ax.set_ylabel("Реальный класс")
                ax.set_title(f"Матрица ошибок: {metrics[key]['name']}")
                for i in range(2):
                    for j in range(2):
                        ax.text(j, i, str(cm[i, j]), ha="center", va="center",
                                color="white" if cm[i, j] > cm.max() / 2 else "black", fontsize=14, fontweight="bold")

        elif idx == 4 and self.last_olap_df is not None:
            numeric_df = self.last_olap_df.set_index(self.last_olap_df.columns[0]).select_dtypes(include=[np.number])
            im = ax.imshow(numeric_df.values, aspect="auto", cmap="YlGnBu")
            self.figure.colorbar(im, ax=ax)
            ax.set_yticks(range(len(numeric_df.index)))
            ax.set_yticklabels([str(i) for i in numeric_df.index], fontsize=8)
            ax.set_xticks(range(len(numeric_df.columns)))
            ax.set_xticklabels([str(c) for c in numeric_df.columns], rotation=20, fontsize=8)
            ax.set_title("Тепловая карта OLAP-куба")

        self.figure.tight_layout()
        self.canvas.draw()

    @Slot()
    def _refresh_history(self):
        source_filter = self.ui.combo_history_source.currentText()
        records = self.pred_service.db.get_records(source_filter)
        cols = ["ID", "Дата и время", "Источник", "Модель", "Параметры", "Вероятность", "Прогноз"]
        df_hist = pd.DataFrame(records, columns=cols) if records else pd.DataFrame(columns=cols)
        self._fill_table(self.ui.table_history, df_hist)

    @Slot()
    def on_clear_history(self):
        self.pred_service.db.clear_records()
        self._refresh_history()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
