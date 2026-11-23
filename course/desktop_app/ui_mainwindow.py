# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 700)
        MainWindow.setMinimumSize(QSize(1182, 700))
        MainWindow.setMaximumSize(QSize(1182, 700))
        MainWindow.setStyleSheet(u"QTabBar::tab {\n"
"    background: #e0e0e0;\n"
"    color: #333333;\n"
"    min-width: 190px;\n"
"    min-height: 45px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #2b5b84;\n"
"    color: white;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 2px solid #2b5b84;\n"
"    border-radius: 0px;\n"
"    background-color: #2b5b84;\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"QTabWidget QStackedWidget > QWidget {\n"
"    background-color: #2b5b84;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #e0e0e0;\n"
"    color: #333333;\n"
"    width: 138px;\n"
"    height: 48px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    margin-right: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #2b5b84;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #d0d8e0;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    color: #333333;\n"
"    min-height: 45px;\n"
"    font-size: 16px;\n"
"    font-wei"
                        "ght: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d8e0;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    color: #222222;\n"
"    border-radius: 6px;\n"
"    gridline-color: #dcdcdc;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eef3f8;\n"
"    color: #2b5b84;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 1px solid #d0d7de;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_widget = QTabWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setStyleSheet(u"QWidget#data {\n"
"    background-color: #2b5b84;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 4px 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    color: #333333;\n"
"    min-height: 45px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d8e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2b5b84;\n"
"    color: white;\n"
"    border: 2px solid #e0e0e0;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    color: #222222;\n"
"    border-radius: 6px;\n"
"    gridline-color: #dcdcdc;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eef3f8;\n"
"    color: #2b5b84;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 1px solid #d0d7de;\n"
"}\n"
"")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.lbl_data_status = QLabel(self.data)
        self.lbl_data_status.setObjectName(u"lbl_data_status")
        self.lbl_data_status.setGeometry(QRect(10, 80, 251, 20))
        font = QFont()
        font.setBold(True)
        self.lbl_data_status.setFont(font)
        self.table_data = QTableWidget(self.data)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setGeometry(QRect(10, 130, 1131, 431))
        self.widget = QWidget(self.data)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1131, 51))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_load_csv = QPushButton(self.widget)
        self.btn_load_csv.setObjectName(u"btn_load_csv")

        self.horizontalLayout.addWidget(self.btn_load_csv)

        self.btn_preprocess = QPushButton(self.widget)
        self.btn_preprocess.setObjectName(u"btn_preprocess")

        self.horizontalLayout.addWidget(self.btn_preprocess)

        self.btn_batch_predict = QPushButton(self.widget)
        self.btn_batch_predict.setObjectName(u"btn_batch_predict")

        self.horizontalLayout.addWidget(self.btn_batch_predict)

        self.btn_export_csv = QPushButton(self.widget)
        self.btn_export_csv.setObjectName(u"btn_export_csv")

        self.horizontalLayout.addWidget(self.btn_export_csv)

        self.table_widget.addTab(self.data, "")
        self.OLAP = QWidget()
        self.OLAP.setObjectName(u"OLAP")
        self.table_olap = QTableWidget(self.OLAP)
        self.table_olap.setObjectName(u"table_olap")
        self.table_olap.setGeometry(QRect(10, 260, 256, 192))
        self.lbl_olap_summary = QLabel(self.OLAP)
        self.lbl_olap_summary.setObjectName(u"lbl_olap_summary")
        self.lbl_olap_summary.setGeometry(QRect(400, 260, 63, 20))
        self.widget1 = QWidget(self.OLAP)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 721, 215))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.combo_olap_rows = QComboBox(self.widget1)
        self.combo_olap_rows.setObjectName(u"combo_olap_rows")

        self.gridLayout.addWidget(self.combo_olap_rows, 0, 0, 1, 1)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.combo_olap_filter_gender = QComboBox(self.widget1)
        self.combo_olap_filter_gender.setObjectName(u"combo_olap_filter_gender")

        self.gridLayout.addWidget(self.combo_olap_filter_gender, 0, 2, 1, 1)

        self.combo_olap_cols = QComboBox(self.widget1)
        self.combo_olap_cols.setObjectName(u"combo_olap_cols")

        self.gridLayout.addWidget(self.combo_olap_cols, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.btn_olap_build = QPushButton(self.widget1)
        self.btn_olap_build.setObjectName(u"btn_olap_build")

        self.gridLayout.addWidget(self.btn_olap_build, 1, 2, 1, 1)

        self.combo_olap_measure = QComboBox(self.widget1)
        self.combo_olap_measure.setObjectName(u"combo_olap_measure")

        self.gridLayout.addWidget(self.combo_olap_measure, 2, 0, 2, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.btn_olap_random = QPushButton(self.widget1)
        self.btn_olap_random.setObjectName(u"btn_olap_random")

        self.gridLayout.addWidget(self.btn_olap_random, 3, 2, 2, 1)

        self.combo_olap_agg = QComboBox(self.widget1)
        self.combo_olap_agg.setObjectName(u"combo_olap_agg")

        self.gridLayout.addWidget(self.combo_olap_agg, 4, 0, 1, 1)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.table_widget.addTab(self.OLAP, "")
        self.predicts = QWidget()
        self.predicts.setObjectName(u"predicts")
        self.gridLayout_2 = QGridLayout(self.predicts)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_model_metrics_4 = QLabel(self.predicts)
        self.lbl_model_metrics_4.setObjectName(u"lbl_model_metrics_4")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_4, 2, 0, 1, 1)

        self.spin_time = QDoubleSpinBox(self.predicts)
        self.spin_time.setObjectName(u"spin_time")

        self.gridLayout_2.addWidget(self.spin_time, 1, 2, 1, 1)

        self.spin_month = QSpinBox(self.predicts)
        self.spin_month.setObjectName(u"spin_month")

        self.gridLayout_2.addWidget(self.spin_month, 2, 5, 1, 1)

        self.combo_gender = QComboBox(self.predicts)
        self.combo_gender.setObjectName(u"combo_gender")

        self.gridLayout_2.addWidget(self.combo_gender, 1, 5, 1, 1)

        self.spin_hour = QSpinBox(self.predicts)
        self.spin_hour.setObjectName(u"spin_hour")

        self.gridLayout_2.addWidget(self.spin_hour, 4, 5, 1, 1)

        self.combo_model = QComboBox(self.predicts)
        self.combo_model.setObjectName(u"combo_model")

        self.gridLayout_2.addWidget(self.combo_model, 0, 1, 1, 2)

        self.lbl_model_metrics_8 = QLabel(self.predicts)
        self.lbl_model_metrics_8.setObjectName(u"lbl_model_metrics_8")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_8, 3, 3, 1, 2)

        self.lbl_predict_result_2 = QLabel(self.predicts)
        self.lbl_predict_result_2.setObjectName(u"lbl_predict_result_2")

        self.gridLayout_2.addWidget(self.lbl_predict_result_2, 0, 0, 1, 1)

        self.lbl_model_metrics_3 = QLabel(self.predicts)
        self.lbl_model_metrics_3.setObjectName(u"lbl_model_metrics_3")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_3, 0, 3, 1, 3)

        self.lbl_model_metrics_5 = QLabel(self.predicts)
        self.lbl_model_metrics_5.setObjectName(u"lbl_model_metrics_5")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_5, 3, 0, 1, 2)

        self.lbl_predict_result = QLabel(self.predicts)
        self.lbl_predict_result.setObjectName(u"lbl_predict_result")

        self.gridLayout_2.addWidget(self.lbl_predict_result, 6, 0, 1, 3)

        self.spin_age = QSpinBox(self.predicts)
        self.spin_age.setObjectName(u"spin_age")

        self.gridLayout_2.addWidget(self.spin_age, 2, 2, 1, 1)

        self.lbl_model_metrics = QLabel(self.predicts)
        self.lbl_model_metrics.setObjectName(u"lbl_model_metrics")

        self.gridLayout_2.addWidget(self.lbl_model_metrics, 1, 3, 1, 2)

        self.spin_internet = QDoubleSpinBox(self.predicts)
        self.spin_internet.setObjectName(u"spin_internet")

        self.gridLayout_2.addWidget(self.spin_internet, 4, 2, 1, 1)

        self.lbl_model_metrics_2 = QLabel(self.predicts)
        self.lbl_model_metrics_2.setObjectName(u"lbl_model_metrics_2")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_2, 1, 0, 1, 2)

        self.spin_income = QDoubleSpinBox(self.predicts)
        self.spin_income.setObjectName(u"spin_income")

        self.gridLayout_2.addWidget(self.spin_income, 3, 2, 1, 1)

        self.lbl_model_metrics_7 = QLabel(self.predicts)
        self.lbl_model_metrics_7.setObjectName(u"lbl_model_metrics_7")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_7, 2, 3, 1, 2)

        self.lbl_model_metrics_6 = QLabel(self.predicts)
        self.lbl_model_metrics_6.setObjectName(u"lbl_model_metrics_6")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_6, 4, 0, 1, 2)

        self.spin_dow = QSpinBox(self.predicts)
        self.spin_dow.setObjectName(u"spin_dow")

        self.gridLayout_2.addWidget(self.spin_dow, 3, 5, 1, 1)

        self.lbl_model_metrics_9 = QLabel(self.predicts)
        self.lbl_model_metrics_9.setObjectName(u"lbl_model_metrics_9")

        self.gridLayout_2.addWidget(self.lbl_model_metrics_9, 4, 3, 1, 2)

        self.btn_predict = QPushButton(self.predicts)
        self.btn_predict.setObjectName(u"btn_predict")

        self.gridLayout_2.addWidget(self.btn_predict, 5, 0, 1, 6)

        self.table_widget.addTab(self.predicts, "")
        self.visual = QWidget()
        self.visual.setObjectName(u"visual")
        self.widget_plot = QTableWidget(self.visual)
        self.widget_plot.setObjectName(u"widget_plot")
        self.widget_plot.setGeometry(QRect(495, 141, 641, 411))
        self.widget_plot_2 = QWidget(self.visual)
        self.widget_plot_2.setObjectName(u"widget_plot_2")
        self.widget_plot_2.setGeometry(QRect(19, 30, 451, 521))
        self.table_metrics_2 = QTableWidget(self.widget_plot_2)
        self.table_metrics_2.setObjectName(u"table_metrics_2")
        self.table_metrics_2.setGeometry(QRect(40, 0, 421, 521))
        self.widget2 = QWidget(self.visual)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(490, 30, 641, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.combo_plot_type = QComboBox(self.widget2)
        self.combo_plot_type.setObjectName(u"combo_plot_type")

        self.horizontalLayout_2.addWidget(self.combo_plot_type)

        self.btn_draw_plot = QPushButton(self.widget2)
        self.btn_draw_plot.setObjectName(u"btn_draw_plot")

        self.horizontalLayout_2.addWidget(self.btn_draw_plot)

        self.table_widget.addTab(self.visual, "")
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.table_history = QTableWidget(self.history)
        self.table_history.setObjectName(u"table_history")
        self.table_history.setGeometry(QRect(20, 81, 1111, 471))
        self.widget3 = QWidget(self.history)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(20, 10, 1121, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.combo_history_source = QComboBox(self.widget3)
        self.combo_history_source.setObjectName(u"combo_history_source")

        self.horizontalLayout_3.addWidget(self.combo_history_source)

        self.btn_clear_history = QPushButton(self.widget3)
        self.btn_clear_history.setObjectName(u"btn_clear_history")

        self.horizontalLayout_3.addWidget(self.btn_clear_history)

        self.btn_refresh_history = QPushButton(self.widget3)
        self.btn_refresh_history.setObjectName(u"btn_refresh_history")

        self.horizontalLayout_3.addWidget(self.btn_refresh_history)

        self.table_widget.addTab(self.history, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.lbl_about_text = QLabel(self.about)
        self.lbl_about_text.setObjectName(u"lbl_about_text")
        self.lbl_about_text.setGeometry(QRect(60, 20, 1021, 501))
        self.lbl_about_text.setWordWrap(True)
        self.table_widget.addTab(self.about, "")

        self.verticalLayout_2.addWidget(self.table_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.table_widget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_data_status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430 \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.btn_load_csv.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c CSV", None))
        self.btn_preprocess.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.btn_batch_predict.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u0434\u043b\u044f \u0432\u0441\u0435\u0445", None))
        self.btn_export_csv.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 CSV", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.data), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.lbl_olap_summary.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0438 \u043a\u0443\u0431\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0446\u044b \u043a\u0443\u0431\u0430", None))
        self.btn_olap_build.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u0443\u0431", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0440\u0430", None))
        self.btn_olap_random.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u0441\u0440\u0435\u0437", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.OLAP), QCoreApplication.translate("MainWindow", u"OLAP", None))
        self.lbl_model_metrics_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.lbl_model_metrics_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.lbl_predict_result_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.lbl_model_metrics_3.setText(QCoreApplication.translate("MainWindow", u"Accuracy: - | F1: -", None))
        self.lbl_model_metrics_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 \u0440\u0435\u0433\u0438\u043e\u043d\u0430", None))
        self.lbl_predict_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c", None))
        self.lbl_model_metrics.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.lbl_model_metrics_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435", None))
        self.lbl_model_metrics_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.lbl_model_metrics_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0444\u0438\u043a \u0432 \u0434\u0435\u043d\u044c", None))
        self.lbl_model_metrics_9.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441", None))
        self.btn_predict.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043a\u043b\u0438\u043a\u0430", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.predicts), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f", None))
        self.btn_draw_plot.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.visual), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.btn_clear_history.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.btn_refresh_history.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0437 \u0411\u0414", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.history), QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.lbl_about_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0442\u043a\u043b\u0438\u043a\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u0440\u0435\u043a\u043b\u0430\u043c\u0443</p><p><br/></p><p>\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f:</p><p>\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d \u0434\u043b\u044f \u043c\u043d\u043e\u0433\u043e\u043c\u0435\u0440\u043d\u043e\u0433\u043e \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438 (OLAP) \u0438"
                        " \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0438 \u043a\u043b\u0438\u043a\u0430 \u043f\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u043c\u0443 \u0431\u0430\u043d\u043d\u0435\u0440\u0443 (Clicked on Ad) \u043c\u0435\u0442\u043e\u0434\u0430\u043c\u0438 \u043c\u0430\u0448\u0438\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f.</p><p><br/></p><p>\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u0441 \u0432\u043a\u043b\u0430\u0434\u043a\u0430\u043c\u0438:</p><p>1. \u0414\u0430\u043d\u043d\u044b\u0435 \u2014 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430 (advertising.csv), \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0447\u0438\u0441\u0442\u043a\u0430"
                        " \u0438 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u043e\u0432 (\u043c\u0435\u0441\u044f\u0446, \u0434\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438, \u0447\u0430\u0441, \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430), \u043f\u0430\u043a\u0435\u0442\u043d\u043e\u0435 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u044d\u043a\u0441\u043f\u043e\u0440\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0432 CSV.</p><p>2. OLAP \u2014 \u0438\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440 \u043c\u043d\u043e\u0433\u043e\u043c\u0435\u0440\u043d\u043e\u0433\u043e \u043a\u0443\u0431\u0430. \u041f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432"
                        "\u0430\u0442\u044c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0435 \u0441\u0440\u0435\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u043c \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c (\u0441\u0442\u0440\u043e\u043a\u0438 \u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b), \u043c\u0435\u0440\u0430\u043c \u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0435 \u0441\u0440\u0435\u0437\u044b.</p><p>3. \u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u2014 \u043e\u0446\u0435\u043d\u043a\u0430 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0438 \u043a\u043b\u0438\u043a\u0430 \u0434\u043b\u044f \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0433\u043e"
                        " \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u043f\u043e 8 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c \u0441 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c\u044e \u0432\u044b\u0431\u043e\u0440\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u043d\u043e\u0439 ML-\u043c\u043e\u0434\u0435\u043b\u0438 \u0438\u043b\u0438 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430.</p><p>4. \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u2014 \u0441\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u043c\u0435\u0442\u0440\u0438\u043a \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u043c\u043e\u0434\u0435\u043b\u0435\u0439 (Accuracy, Precision, Recall, F1-score) \u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 (\u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435"
                        " \u043c\u043e\u0434\u0435\u043b\u0435\u0439, \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u043e\u0448\u0438\u0431\u043e\u043a, \u0442\u0435\u043f\u043b\u043e\u0432\u0430\u044f \u043a\u0430\u0440\u0442\u0430 OLAP-\u043a\u0443\u0431\u0430).</p><p>5. \u0418\u0441\u0442\u043e\u0440\u0438\u044f \u2014 \u0436\u0443\u0440\u043d\u0430\u043b \u0432\u0441\u0435\u0445 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432 \u0438\u0437 \u043e\u0431\u0449\u0435\u0439 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 SQLite3 (\u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441 Telegram-\u0431\u043e\u0442\u043e\u043c).</p><p><br/></p><p>\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0430 \u0438 \u0441\u0442\u0435\u043a \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439:</p><p>\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0440\u043e\u0435"
                        "\u043d\u043e \u043f\u043e \u043c\u043d\u043e\u0433\u043e\u0441\u043b\u043e\u0439\u043d\u043e\u0439 \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0435 (Layered Architecture) \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435\u043c \u0441\u043b\u043e\u044f \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f (PySide6 / aiogram 3), \u0441\u0435\u0440\u0432\u0438\u0441\u043d\u043e\u0433\u043e \u0441\u043b\u043e\u044f, ML-\u044f\u0434\u0440\u0430 \u0438 \u0441\u043b\u043e\u044f \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445.</p><p>\u2022 \u042f\u0437\u044b\u043a \u0438 GUI: Python 3, PySide6 (Qt Designer)</p><p>\u2022 \u0410\u043d\u0430\u043b\u0438\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 ML: pandas, NumPy, scikit-learn, joblib, Matplotlib</p><p>\u2022 \u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0438\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f: SQLite3, Telegram Bot API (ai"
                        "ogram 3)</p></body></html>", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.about), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

