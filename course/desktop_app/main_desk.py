import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QTabWidget, QPushButton, QLabel, 
                               QLineEdit, QTableWidget, QTableWidgetItem, 
                               QFileDialog, QMessageBox, QHeaderView)
from PySide6.QtCore import Qt
import pandas as pd

# Импорт вашей бизнес-логики (файл business_logic.py должен лежать рядом)
from business_logic import load_csv, preprocess, load_model, predict_user


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Прогнозирование кликов по рекламе")
        self.resize(900, 600)
        
        self.df = None
        self.model = None
        
        # Центральный виджет и вкладки
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Создание вкладок
        self._create_data_tab()
        self._create_predict_tab()
        self._create_about_tab()
        
        # Попытка загрузить модель при старте
        self._try_load_model()

    def _create_data_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        btn_layout = QHBoxLayout()
        self.btn_load = QPushButton("📂 Загрузить CSV")
        self.btn_preprocess = QPushButton("⚙️ Предобработать")
        self.lbl_status = QLabel("Данные не загружены")
        
        self.btn_load.clicked.connect(self.load_csv_handler)
        self.btn_preprocess.clicked.connect(self.preprocess_handler)
        
        btn_layout.addWidget(self.btn_load)
        btn_layout.addWidget(self.btn_preprocess)
        btn_layout.addStretch()
        btn_layout.addWidget(self.lbl_status)
        
        self.table_data = QTableWidget()
        self.table_data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addLayout(btn_layout)
        layout.addWidget(self.table_data)
        self.tabs.addTab(tab, "📁 Данные")

    def _create_predict_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        form_layout = QVBoxLayout()
        fields = [
            ('Daily Time Spent on Site', '65.0'),
            ('Age', '35'),
            ('Area Income', '55000.0'),
            ('Daily Internet Usage', '180.0'),
            ('Male', '0'),
            ('Month', '3'),
            ('DayOfWeek', '6'),
            ('Hour', '10'),
        ]
        
        self.entries = {}
        for name, default in fields:
            row = QHBoxLayout()
            label = QLabel(f"{name}:")
            entry = QLineEdit(default)
            self.entries[name] = entry
            row.addWidget(label)
            row.addWidget(entry)
            form_layout.addLayout(row)
            
        self.btn_predict = QPushButton("🎯 Предсказать")
        self.btn_predict.clicked.connect(self.predict_handler)
        self.lbl_result = QLabel("Результат появится здесь...")
        self.lbl_result.setAlignment(Qt.AlignCenter)
        self.lbl_result.setStyleSheet("font-size: 16px; font-weight: bold; color: blue; padding: 20px;")
        
        layout.addLayout(form_layout)
        layout.addWidget(self.btn_predict)
        layout.addWidget(self.lbl_result)
        layout.addStretch()
        self.tabs.addTab(tab, "🎯 Предсказание")

    def _create_about_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        text = QLabel(
            "<h2>Система прогнозирования кликов</h2>"
            "<p>Приложение разработано в рамках курсовой работы.</p>"
            "<p><b>Модель:</b> Логистическая регрессия (scikit-learn)</p>"
            "<p><b>Точность:</b> 97.5%</p>"
            "<p><b>Интерфейс:</b> PySide6 (Qt for Python)</p>"
        )
        text.setAlignment(Qt.AlignCenter)
        layout.addWidget(text)
        self.tabs.addTab(tab, "ℹ️ О программе")

    def _try_load_model(self):
        # Ищем модель в папке models рядом с этим скриптом
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'models', 'lr_model.pkl')
        
        if os.path.exists(model_path):
            try:
                self.model = load_model(model_path)
                self.lbl_status.setText("✅ Модель загружена")
            except Exception as e:
                self.lbl_status.setText(f"❌ Ошибка модели: {e}")
        else:
            self.lbl_status.setText("⚠️ Модель не найдена (положите lr_model.pkl в папку models/)")

    def load_csv_handler(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Выберите CSV", "", "CSV Files (*.csv)")
        if not filepath: return
        try:
            self.df = load_csv(filepath)
            self.lbl_status.setText(f"✅ Загружено: {self.df.shape[0]} строк")
            self._display_table(self.df.head(100))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def preprocess_handler(self):
        if self.df is None:
            QMessageBox.warning(self, "Внимание", "Сначала загрузите CSV!")
            return
        try:
            self.df = preprocess(self.df)
            self.lbl_status.setText(f"✅ Предобработано: {self.df.shape[1]} столбцов")
            self._display_table(self.df.head(100))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def _display_table(self, df):
        self.table_data.setRowCount(df.shape[0])
        self.table_data.setColumnCount(df.shape[1])
        self.table_data.setHorizontalHeaderLabels(df.columns.tolist())
        for i, row in enumerate(df.itertuples(index=False)):
            for j, val in enumerate(row):
                self.table_data.setItem(i, j, QTableWidgetItem(str(val)))

    def predict_handler(self):
        if self.model is None:
            QMessageBox.warning(self, "Внимание", "Модель не загружена!")
            return
        try:
            user_data = {}
            for name, entry in self.entries.items():
                val = entry.text().strip()
                user_data[name] = float(val) if '.' in val else int(val)
            
            result = predict_user(self.model, user_data)
            
            if result['class'] == 1:
                msg = f"✅ КЛИКНЕТ (вероятность: {result['probability']:.2%})"
                self.lbl_result.setStyleSheet("font-size: 18px; font-weight: bold; color: green; padding: 20px;")
            else:
                msg = f"❌ НЕ КЛИКНЕТ (вероятность: {result['probability']:.2%})"
                self.lbl_result.setStyleSheet("font-size: 18px; font-weight: bold; color: red; padding: 20px;")
                
            self.lbl_result.setText(msg)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка предсказания", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())