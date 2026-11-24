# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 700)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
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
"    border: none;\n"
"    background-color: #2b5b84;\n"
"    top: 0px;\n"
"}\n"
"\n"
"QTabWidget QStackedWidget > QWidget {\n"
"    background-color: #2b5b84;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #e0e0e0;\n"
"    color: #333333;\n"
"    min-width: 190px;\n"
"    height: 48px;\n"
"    font-size: 17px;\n"
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
"    font-size: 17px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    color: #333333;\n"
"    min-height: 48px;\n"
"    font-size: 17px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    bor"
                        "der-radius: 8px;\n"
"    padding: 0px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d8e0;\n"
"}\n"
"\n"
"QComboBox, QSpinBox, QDoubleSpinBox {\n"
"    background-color: white;\n"
"    color: #222222;\n"
"    min-height: 40px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    color: #222222;\n"
"    border-radius: 6px;\n"
"    gridline-color: #dcdcdc;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #eef3f8;\n"
"    color: #2b5b84;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    border: 1px solid #d0d7de;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    background-color: white;\n"
"    color: #222222;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"    padding: 16px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_widget = QTabWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setStyleSheet(u"")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.verticalLayout = QVBoxLayout(self.data)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_load_csv = QPushButton(self.data)
        self.btn_load_csv.setObjectName(u"btn_load_csv")

        self.horizontalLayout.addWidget(self.btn_load_csv)

        self.btn_preprocess = QPushButton(self.data)
        self.btn_preprocess.setObjectName(u"btn_preprocess")

        self.horizontalLayout.addWidget(self.btn_preprocess)

        self.btn_batch_predict = QPushButton(self.data)
        self.btn_batch_predict.setObjectName(u"btn_batch_predict")

        self.horizontalLayout.addWidget(self.btn_batch_predict)

        self.btn_export_csv = QPushButton(self.data)
        self.btn_export_csv.setObjectName(u"btn_export_csv")

        self.horizontalLayout.addWidget(self.btn_export_csv)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_data_status = QLabel(self.data)
        self.lbl_data_status.setObjectName(u"lbl_data_status")
        font = QFont()
        font.setBold(True)
        self.lbl_data_status.setFont(font)
        self.lbl_data_status.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_data_status)

        self.table_data = QTableWidget(self.data)
        self.table_data.setObjectName(u"table_data")

        self.verticalLayout.addWidget(self.table_data)

        self.table_widget.addTab(self.data, "")
        self.OLAP = QWidget()
        self.OLAP.setObjectName(u"OLAP")
        self.verticalLayout_3 = QVBoxLayout(self.OLAP)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.combo_olap_rows = QComboBox(self.OLAP)
        self.combo_olap_rows.setObjectName(u"combo_olap_rows")

        self.gridLayout.addWidget(self.combo_olap_rows, 0, 0, 1, 1)

        self.label = QLabel(self.OLAP)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.combo_olap_filter_gender = QComboBox(self.OLAP)
        self.combo_olap_filter_gender.setObjectName(u"combo_olap_filter_gender")

        self.gridLayout.addWidget(self.combo_olap_filter_gender, 0, 2, 1, 1)

        self.combo_olap_cols = QComboBox(self.OLAP)
        self.combo_olap_cols.setObjectName(u"combo_olap_cols")

        self.gridLayout.addWidget(self.combo_olap_cols, 1, 0, 1, 1)

        self.label_2 = QLabel(self.OLAP)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.btn_olap_build = QPushButton(self.OLAP)
        self.btn_olap_build.setObjectName(u"btn_olap_build")

        self.gridLayout.addWidget(self.btn_olap_build, 1, 2, 1, 1)

        self.combo_olap_measure = QComboBox(self.OLAP)
        self.combo_olap_measure.setObjectName(u"combo_olap_measure")

        self.gridLayout.addWidget(self.combo_olap_measure, 2, 0, 2, 1)

        self.label_3 = QLabel(self.OLAP)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.btn_olap_random = QPushButton(self.OLAP)
        self.btn_olap_random.setObjectName(u"btn_olap_random")

        self.gridLayout.addWidget(self.btn_olap_random, 3, 2, 2, 1)

        self.combo_olap_agg = QComboBox(self.OLAP)
        self.combo_olap_agg.setObjectName(u"combo_olap_agg")

        self.gridLayout.addWidget(self.combo_olap_agg, 4, 0, 1, 1)

        self.label_4 = QLabel(self.OLAP)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.lbl_olap_summary = QLabel(self.OLAP)
        self.lbl_olap_summary.setObjectName(u"lbl_olap_summary")
        self.lbl_olap_summary.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lbl_olap_summary)

        self.table_olap = QTableWidget(self.OLAP)
        self.table_olap.setObjectName(u"table_olap")

        self.verticalLayout_3.addWidget(self.table_olap)

        self.table_widget.addTab(self.OLAP, "")
        self.predicts = QWidget()
        self.predicts.setObjectName(u"predicts")
        self.verticalLayout_4 = QVBoxLayout(self.predicts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_predict_result_2 = QLabel(self.predicts)
        self.lbl_predict_result_2.setObjectName(u"lbl_predict_result_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_predict_result_2)

        self.lbl_model_metrics_2 = QLabel(self.predicts)
        self.lbl_model_metrics_2.setObjectName(u"lbl_model_metrics_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_2)

        self.spin_time = QDoubleSpinBox(self.predicts)
        self.spin_time.setObjectName(u"spin_time")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spin_time)

        self.lbl_model_metrics_4 = QLabel(self.predicts)
        self.lbl_model_metrics_4.setObjectName(u"lbl_model_metrics_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_4)

        self.spin_age = QSpinBox(self.predicts)
        self.spin_age.setObjectName(u"spin_age")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spin_age)

        self.lbl_model_metrics_5 = QLabel(self.predicts)
        self.lbl_model_metrics_5.setObjectName(u"lbl_model_metrics_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_5)

        self.spin_income = QDoubleSpinBox(self.predicts)
        self.spin_income.setObjectName(u"spin_income")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spin_income)

        self.lbl_model_metrics_6 = QLabel(self.predicts)
        self.lbl_model_metrics_6.setObjectName(u"lbl_model_metrics_6")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_6)

        self.spin_internet = QDoubleSpinBox(self.predicts)
        self.spin_internet.setObjectName(u"spin_internet")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spin_internet)

        self.combo_model = QComboBox(self.predicts)
        self.combo_model.setObjectName(u"combo_model")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combo_model)


        self.horizontalLayout_4.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.combo_gender = QComboBox(self.predicts)
        self.combo_gender.setObjectName(u"combo_gender")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_gender)

        self.lbl_model_metrics = QLabel(self.predicts)
        self.lbl_model_metrics.setObjectName(u"lbl_model_metrics")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics)

        self.lbl_model_metrics_7 = QLabel(self.predicts)
        self.lbl_model_metrics_7.setObjectName(u"lbl_model_metrics_7")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_7)

        self.spin_month = QSpinBox(self.predicts)
        self.spin_month.setObjectName(u"spin_month")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spin_month)

        self.lbl_model_metrics_8 = QLabel(self.predicts)
        self.lbl_model_metrics_8.setObjectName(u"lbl_model_metrics_8")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_8)

        self.spin_dow = QSpinBox(self.predicts)
        self.spin_dow.setObjectName(u"spin_dow")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spin_dow)

        self.lbl_model_metrics_9 = QLabel(self.predicts)
        self.lbl_model_metrics_9.setObjectName(u"lbl_model_metrics_9")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_model_metrics_9)

        self.spin_hour = QSpinBox(self.predicts)
        self.spin_hour.setObjectName(u"spin_hour")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spin_hour)

        self.lbl_model_metrics_3 = QLabel(self.predicts)
        self.lbl_model_metrics_3.setObjectName(u"lbl_model_metrics_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.lbl_model_metrics_3)


        self.horizontalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.btn_predict = QPushButton(self.predicts)
        self.btn_predict.setObjectName(u"btn_predict")

        self.verticalLayout_4.addWidget(self.btn_predict)

        self.lbl_predict_result = QLabel(self.predicts)
        self.lbl_predict_result.setObjectName(u"lbl_predict_result")

        self.verticalLayout_4.addWidget(self.lbl_predict_result)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.table_widget.addTab(self.predicts, "")
        self.visual = QWidget()
        self.visual.setObjectName(u"visual")
        self.gridLayout_4 = QGridLayout(self.visual)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_plot_2 = QWidget(self.visual)
        self.widget_plot_2.setObjectName(u"widget_plot_2")
        self.gridLayout_3 = QGridLayout(self.widget_plot_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_metrics_2 = QTableWidget(self.widget_plot_2)
        self.table_metrics_2.setObjectName(u"table_metrics_2")

        self.gridLayout_3.addWidget(self.table_metrics_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_plot_2, 0, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_plot_type = QComboBox(self.visual)
        self.combo_plot_type.setObjectName(u"combo_plot_type")

        self.horizontalLayout_2.addWidget(self.combo_plot_type)

        self.btn_draw_plot = QPushButton(self.visual)
        self.btn_draw_plot.setObjectName(u"btn_draw_plot")

        self.horizontalLayout_2.addWidget(self.btn_draw_plot)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.widget_plot = QTableWidget(self.visual)
        self.widget_plot.setObjectName(u"widget_plot")

        self.gridLayout_4.addWidget(self.widget_plot, 1, 1, 1, 1)

        self.table_widget.addTab(self.visual, "")
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_5 = QVBoxLayout(self.history)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.combo_history_source = QComboBox(self.history)
        self.combo_history_source.setObjectName(u"combo_history_source")

        self.horizontalLayout_3.addWidget(self.combo_history_source)

        self.btn_clear_history = QPushButton(self.history)
        self.btn_clear_history.setObjectName(u"btn_clear_history")

        self.horizontalLayout_3.addWidget(self.btn_clear_history)

        self.btn_refresh_local = QPushButton(self.history)
        self.btn_refresh_local.setObjectName(u"btn_refresh_local")

        self.horizontalLayout_3.addWidget(self.btn_refresh_local)

        self.btn_refresh_tg = QPushButton(self.history)
        self.btn_refresh_tg.setObjectName(u"btn_refresh_tg")

        self.horizontalLayout_3.addWidget(self.btn_refresh_tg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.table_history = QTableWidget(self.history)
        self.table_history.setObjectName(u"table_history")

        self.verticalLayout_5.addWidget(self.table_history)

        self.table_widget.addTab(self.history, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_6 = QVBoxLayout(self.about)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.text_about = QTextBrowser(self.about)
        self.text_about.setObjectName(u"text_about")
        self.text_about.setStyleSheet(u"QTextBrowser {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-size: 17px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.text_about)

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
        self.btn_load_csv.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c CSV", None))
        self.btn_preprocess.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.btn_batch_predict.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u0434\u043b\u044f \u0432\u0441\u0435\u0445", None))
        self.btn_export_csv.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 CSV", None))
        self.lbl_data_status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430 \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.data), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0438 \u043a\u0443\u0431\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0446\u044b \u043a\u0443\u0431\u0430", None))
        self.btn_olap_build.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u0443\u0431", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0440\u0430", None))
        self.btn_olap_random.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u0441\u0440\u0435\u0437", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f", None))
        self.lbl_olap_summary.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.OLAP), QCoreApplication.translate("MainWindow", u"OLAP", None))
        self.lbl_predict_result_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.lbl_model_metrics_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435", None))
        self.lbl_model_metrics_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.lbl_model_metrics_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 \u0440\u0435\u0433\u0438\u043e\u043d\u0430", None))
        self.lbl_model_metrics_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0444\u0438\u043a \u0432 \u0434\u0435\u043d\u044c", None))
        self.lbl_model_metrics.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.lbl_model_metrics_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.lbl_model_metrics_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.lbl_model_metrics_9.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441", None))
        self.lbl_model_metrics_3.setText(QCoreApplication.translate("MainWindow", u"Accuracy: - | F1: -", None))
        self.btn_predict.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043a\u043b\u0438\u043a\u0430", None))
        self.lbl_predict_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.predicts), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f", None))
        self.btn_draw_plot.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.visual), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.btn_clear_history.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.btn_refresh_local.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.btn_refresh_tg.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 Telegram", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.history), QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.text_about.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:17px; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u0421\u0418\u0421\u0422\u0415\u041c\u0410 \u0410\u041d\u0410\u041b\u0418\u0417\u0410 \u0418 \u041f\u0420\u041e\u0413\u041d\u041e\u0417\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f \u041e\u0422\u041a\u041b\u0418\u041a\u0410 \u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u0422\u0415\u041b\u0415\u0419 \u041d\u0410 \u0418\u041d\u0422\u0415\u0420\u041d"
                        "\u0415\u0422-\u0420\u0415\u041a\u041b\u0410\u041c\u0423</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d \u0434\u043b\u044f \u043c\u043d\u043e\u0433\u043e\u043c\u0435\u0440\u043d\u043e\u0433\u043e"
                        " \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438 (OLAP) \u0438 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0438 \u043a\u043b\u0438\u043a\u0430 \u043f\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u043c\u0443 \u0431\u0430\u043d\u043d\u0435\u0440\u0443 (Clicked on Ad) \u043c\u0435\u0442\u043e\u0434\u0430\u043c\u0438 \u043c\u0430\u0448\u0438\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:"
                        "400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u041f\u041e\u0414\u0420\u041e\u0411\u041d\u041e\u0415 \u0420\u0423\u041a\u041e\u0412\u041e\u0414\u0421\u0422\u0412\u041e \u041f\u041e \u042d\u041b\u0415\u041c\u0415\u041d\u0422\u0410\u041c \u0423\u041f\u0420\u0410\u0412\u041b\u0415\u041d\u0418\u042f</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">1. \u0412\u043a\u043b\u0430\u0434\u043a\u0430 \u00ab\u0414\u0430\u043d\u043d\u044b\u0435\u00bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c CSV \u2014 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0435 \u0434\u0438\u0430\u043b\u043e\u0433\u0430 \u0432\u044b\u0431\u043e\u0440\u0430 \u0444\u0430\u0439\u043b\u0430 \u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430 (\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e advertising.csv) \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u043f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u2014 \u043e\u0447\u0438\u0441\u0442\u043a\u0430 \u0434\u0430"
                        "\u043d\u043d\u044b\u0445 \u043e\u0442 \u043d\u0435\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 (Ad Topic Line, City), \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0438\u0437 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u043c\u0435\u0442\u043a\u0438 Timestamp \u043c\u0435\u0441\u044f\u0446\u0430, \u0434\u043d\u044f \u043d\u0435\u0434\u0435\u043b\u0438 \u0438 \u0447\u0430\u0441\u0430, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430 \u043d\u0430 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u044b\u0435 \u0433\u0440\u0443\u043f\u043f\u044b (Age_Group).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u0434\u043b\u044f "
                        "\u0432\u0441\u0435\u0445 \u2014 \u043f\u0430\u043a\u0435\u0442\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0438 \u043a\u043b\u0438\u043a\u0430 \u0441\u0440\u0430\u0437\u0443 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0438\u0437 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u043c\u043e\u0434\u0435\u043b\u0438, \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u00ab\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f\u00bb. \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u0442\u043e\u043b\u0431\u0446\u044b Predicted_Click \u0438 Click_Probability.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 CSV \u2014 \u044d\u043a\u0441\u043f\u043e\u0440\u0442 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0432\u043c\u0435\u0441\u0442\u0435 \u0441 \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u043c\u0438 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0430\u043c\u0438 \u0432 \u043d\u043e\u0432\u044b\u0439 CSV-\u0444\u0430\u0439\u043b \u043d\u0430 \u0434\u0438\u0441\u043a.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">2. \u0412\u043a\u043b\u0430"
                        "\u0434\u043a\u0430 \u00abOLAP\u00bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0421\u0442\u0440\u043e\u043a\u0438 \u043a\u0443\u0431\u0430 / \u0421\u0442\u043e\u043b\u0431\u0446\u044b \u043a\u0443\u0431\u0430 \u2014 \u0432\u044b\u0431\u043e\u0440 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0439 (\u043e\u0441\u0435\u0439) \u043c\u043d\u043e\u0433\u043e\u043c\u0435\u0440\u043d\u043e\u0433\u043e \u043a\u0443\u0431\u0430: \u041c\u0435\u0441\u044f\u0446, \u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438, \u0427\u0430\u0441, \u041f\u043e\u043b, \u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430 \u0438\u043b\u0438 \u0421\u0442\u0440\u0430\u043d\u0430 (\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u043e\u043c\u0435\u0440\u043d\u044b\u0439 \u0440\u0435"
                        "\u0436\u0438\u043c \u0431\u0435\u0437 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041c\u0435\u0440\u0430 \u2014 \u0432\u044b\u0431\u043e\u0440 \u0447\u0438\u0441\u043b\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0451\u0442\u0430: \u041a\u043b\u0438\u043a \u043f\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u0435, \u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435, \u0422\u0440\u0430\u0444\u0438\u043a, \u0414\u043e\u0445\u043e\u0434 \u0440\u0435\u0433\u0438\u043e\u043d\u0430 \u0438\u043b\u0438 \u0412\u043e\u0437\u0440\u0430\u0441\u0442.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; f"
                        "ont-weight:400;\">\u2022 \u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f \u2014 \u0432\u044b\u0431\u043e\u0440 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u043c\u0435\u0440\u044b: \u0421\u0440\u0435\u0434\u043d\u0435\u0435 (mean), \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e (count), \u0421\u0443\u043c\u043c\u0430 (sum), \u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c (max) \u0438\u043b\u0438 \u041c\u0438\u043d\u0438\u043c\u0443\u043c (min).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e\u043b\u0430 \u2014 \u0441\u0440\u0435\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u043f\u043e\u043b\u0443 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b"
                        "\u044f (\u0412\u0441\u0435, \u0422\u043e\u043b\u044c\u043a\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u044b \u0438\u043b\u0438 \u0422\u043e\u043b\u044c\u043a\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u044b).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u0443\u0431 \u2014 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u0432\u043e\u0434\u043d\u043e\u0439 OLAP-\u0442\u0430\u0431\u043b\u0438\u0446\u044b \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:4"
                        "00;\">\u2022 \u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u0441\u0440\u0435\u0437 \u2014 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u043e\u0434\u0431\u043e\u0440 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0439 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043e\u0441\u0435\u0439, \u043c\u0435\u0440\u044b \u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0434\u043b\u044f \u0431\u044b\u0441\u0442\u0440\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430 \u0437\u0430\u043a\u043e\u043d\u043e\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u0435\u0439 \u0432 \u0434\u0430\u043d\u043d\u044b\u0445.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-size:16px; font-weight:400;\">3. \u0412\u043a\u043b\u0430\u0434\u043a\u0430 \u00ab\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f\u00bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041c\u043e\u0434\u0435\u043b\u044c \u2014 \u0432\u044b\u0431\u043e\u0440 \u043e\u0431\u0443\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u043c\u0430\u0448\u0438\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (\u041b\u043e\u0433\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0440\u0435\u0433\u0440\u0435\u0441\u0441\u0438\u044f LR, \u0414\u0435\u0440\u0435\u0432\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u0439 DT \u0438\u043b\u0438 \u041d\u0435\u0439\u0440\u043e\u0441\u0435\u0442\u044c MLP) \u0441 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435"
                        "\u043c \u0435\u0451 \u043c\u0435\u0442\u0440\u0438\u043a \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 Accuracy \u0438 F1.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (8 \u043f\u043e\u043b\u0435\u0439) \u2014 \u0432\u0432\u043e\u0434 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438: \u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435 (\u043c\u0438\u043d), \u0412\u043e\u0437\u0440\u0430\u0441\u0442, \u0414\u043e\u0445\u043e\u0434 \u0440\u0435\u0433\u0438\u043e\u043d\u0430, \u0422\u0440\u0430\u0444\u0438\u043a \u0432 \u0434\u0435\u043d\u044c (\u041c\u0411), \u041f\u043e\u043b, \u041c\u0435\u0441\u044f\u0446 (1\u201312), \u0414\u0435"
                        "\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438 (0\u20136) \u0438 \u0427\u0430\u0441 (0\u201323).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043a\u043b\u0438\u043a\u0430 \u2014 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u0430 \u0432 \u0444\u043e\u043d\u043e\u0432\u043e\u043c \u043f\u043e\u0442\u043e\u043a\u0435, \u0432\u044b\u0432\u043e\u0434 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430 \u0438 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438"
                        " \u0432 \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445 history.db.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">4. \u0412\u043a\u043b\u0430\u0434\u043a\u0430 \u00ab\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b\u00bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u043c\u0435\u0442\u0440\u0438\u043a (\u0441\u043b\u0435\u0432\u0430) \u2014 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043a\u0430\u0447\u0435\u0441\u0442"
                        "\u0432\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u043d\u044b\u0445 \u043c\u043e\u0434\u0435\u043b\u0435\u0439 \u043f\u043e \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f\u043c Accuracy, Precision, Recall, F1-score \u0438 ROC-AUC.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0412\u044b\u0431\u043e\u0440 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u2014 \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0440\u0435\u0436\u0438\u043c\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430: \u0441\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u043e\u0434\u0435\u043b\u0435\u0439, \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u043e\u0448\u0438\u0431\u043e\u043a (Confusion Matrix) \u0434\u043b"
                        "\u044f \u043a\u0430\u0436\u0434\u043e\u0439 \u043c\u043e\u0434\u0435\u043b\u0438 \u0438\u043b\u0438 \u0442\u0435\u043f\u043b\u043e\u0432\u0430\u044f \u043a\u0430\u0440\u0442\u0430 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e OLAP-\u043a\u0443\u0431\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u2014 \u043f\u0435\u0440\u0435\u0440\u0438\u0441\u043e\u0432\u043a\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0438\u043b\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0441\u0440\u0435\u0437\u0430 \u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0435"
                        " \u00abOLAP\u00bb.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">5. \u0412\u043a\u043b\u0430\u0434\u043a\u0430 \u00ab\u0418\u0441\u0442\u043e\u0440\u0438\u044f\u00bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0424\u0438\u043b\u044c\u0442\u0440 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430 (\u0412\u0441\u0435 / Desktop / Telegram) \u2014 \u043e\u0442\u0431\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0436\u0443\u0440\u043d\u0430\u043b\u0430 \u043f\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044e,"
                        " \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u044b\u043b \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d \u0437\u0430\u043f\u0440\u043e\u0441.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u2014 \u043f\u043e\u043b\u043d\u043e\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0432\u0441\u0435\u0445 \u0441\u043e\u0445\u0440\u0430\u043d\u0451\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432 \u0438\u0437 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 SQLite3 (history.db).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041e\u0431\u043d\u043e\u0432\u0438\u0442"
                        "\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u2014 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u043d\u043e\u0437\u043e\u0432, \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0432 \u043d\u0430\u0441\u0442\u043e\u043b\u044c\u043d\u043e\u043c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0437 \u0431\u043e\u0442\u0430 \u0432 \u0422\u0413 \u2014 \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432, \u043e\u0442\u043f\u0440\u0430\u0432\u043b"
                        "\u0435\u043d\u043d\u044b\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438 \u0447\u0435\u0440\u0435\u0437 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0451\u043d\u043d\u043e\u0433\u043e Telegram-\u0431\u043e\u0442\u0430.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u0410\u0420\u0425\u0418\u0422\u0415\u041a\u0422\u0423\u0420\u0410 \u0418 \u0421\u0422\u0415\u041a \u0422\u0415\u0425\u041d\u041e\u041b\u041e\u0413\u0418\u0419</span></p>\n"
"<p style=\"-qt-"
                        "paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u043e \u043f\u043e \u043c\u043d\u043e\u0433\u043e\u0441\u043b\u043e\u0439\u043d\u043e\u0439 \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0435 (Layered Architecture) \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435\u043c \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430 (PySide6 / aiogram 3), \u0441\u0435\u0440\u0432\u0438\u0441\u043d\u043e\u0433\u043e \u0441\u043b\u043e\u044f, ML-\u044f\u0434\u0440\u0430 \u0438 \u0441\u043b\u043e\u044f \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b"
                        "\u0445.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u042f\u0437\u044b\u043a \u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441: Python 3, PySide6 (Qt Designer)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0410\u043d\u0430\u043b\u0438\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 ML: pandas, NumPy, scikit-learn, joblib, Matplotlib</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:400;\">\u2022 \u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0438\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f: SQLite3 (history.db), Telegram Bot API (aiogram 3)</sp"
                        "an></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16px; font-weight:400;\"><br /></p></body></html>", None))
        self.table_widget.setTabText(self.table_widget.indexOf(self.about), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

