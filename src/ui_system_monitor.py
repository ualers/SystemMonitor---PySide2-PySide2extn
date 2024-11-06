# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_system_monitor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 718)
        MainWindow.setStyleSheet(u"\n"
"\n"
"/* Central Widget */\n"
"QWidget#centralwidget {\n"
"    background-color: #625d94;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #ECF0F1;\n"
"}\n"
"\n"
"/* Progress Bars */\n"
"QProgressBar {\n"
"    background-color: #34495E;\n"
"    color: #ECF0F1;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #3498DB;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #3498DB;\n"
"    color: #ECF0F1;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980B9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1B4F72;\n"
"}\n"
"\n"
"/* Group Boxes */\n"
"QGroupBox {\n"
"    background-color: #34495E;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-posit"
                        "ion: top center;\n"
"    padding: 0 3px;\n"
"    color: #ECF0F1;\n"
"}\n"
"\n"
"/* Round Progress Bar */\n"
"RoundProgressBar {\n"
"    background-color: #34495E;\n"
"    color: #ECF0F1;\n"
"    border-radius: 50%;\n"
"}\n"
"\n"
"RoundProgressBar[barStyle=\"2\"] {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RoundProgressBar[barStyle=\"2\"]::chunk {\n"
"    border-radius: 50%;\n"
"    background-color: #3498DB;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.myStackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(u"myStackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myStackedWidget.sizePolicy().hasHeightForWidth())
        self.myStackedWidget.setSizePolicy(sizePolicy)
        self.myStackedWidget.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: #1e162b;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1e162b;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_CPU = QLabel(self.frame)
        self.label_CPU.setObjectName(u"label_CPU")
        self.label_CPU.setGeometry(QRect(0, 40, 191, 20))
        self.label_CPU.setMinimumSize(QSize(0, 19))
        self.label_CPU.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(7)
        self.label_CPU.setFont(font)
        self.label_CPU.setMargin(0)
        self.label_CPU.setIndent(0)
        self.widget_cpu = roundProgressBar(self.frame)
        self.widget_cpu.setObjectName(u"widget_cpu")
        self.widget_cpu.setGeometry(QRect(90, 90, 81, 71))
        self.widget_cpu.setMaximumSize(QSize(200, 200))
        self.widget_cpu.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.widget_ram = roundProgressBar(self.frame)
        self.widget_ram.setObjectName(u"widget_ram")
        self.widget_ram.setGeometry(QRect(510, 110, 91, 81))
        self.widget_ram.setMaximumSize(QSize(118, 100))
        self.widget_ram.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_RAM = QLabel(self.frame)
        self.label_RAM.setObjectName(u"label_RAM")
        self.label_RAM.setGeometry(QRect(420, 40, 91, 19))
        sizePolicy.setHeightForWidth(self.label_RAM.sizePolicy().hasHeightForWidth())
        self.label_RAM.setSizePolicy(sizePolicy)
        self.label_RAM.setMinimumSize(QSize(0, 19))
        self.label_RAM.setMaximumSize(QSize(16777215, 18))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_RAM.setFont(font1)
        self.label_RAM.setMargin(0)
        self.label_RAM.setIndent(0)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(190, 0, 16, 641))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(390, 0, 16, 631))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_GPU = QLabel(self.frame)
        self.label_GPU.setObjectName(u"label_GPU")
        self.label_GPU.setGeometry(QRect(210, 40, 161, 20))
        sizePolicy.setHeightForWidth(self.label_GPU.sizePolicy().hasHeightForWidth())
        self.label_GPU.setSizePolicy(sizePolicy)
        self.label_GPU.setMinimumSize(QSize(0, 19))
        self.label_GPU.setMaximumSize(QSize(16777215, 20))
        self.label_GPU.setFont(font)
        self.label_GPU.setMargin(0)
        self.label_GPU.setIndent(0)
        self.widget_gpu = roundProgressBar(self.frame)
        self.widget_gpu.setObjectName(u"widget_gpu")
        self.widget_gpu.setGeometry(QRect(290, 370, 71, 61))
        self.widget_gpu.setMaximumSize(QSize(200, 200))
        self.widget_gpu.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_CPU_2 = QLabel(self.frame)
        self.label_CPU_2.setObjectName(u"label_CPU_2")
        self.label_CPU_2.setGeometry(QRect(0, 0, 191, 19))
        self.label_CPU_2.setMinimumSize(QSize(0, 19))
        self.label_CPU_2.setMaximumSize(QSize(16777215, 20))
        self.label_CPU_2.setFont(font)
        self.label_CPU_2.setMargin(0)
        self.label_CPU_2.setIndent(69)
        self.label_CPU_3 = QLabel(self.frame)
        self.label_CPU_3.setObjectName(u"label_CPU_3")
        self.label_CPU_3.setGeometry(QRect(10, 300, 61, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_CPU_3.sizePolicy().hasHeightForWidth())
        self.label_CPU_3.setSizePolicy(sizePolicy1)
        self.label_CPU_3.setMinimumSize(QSize(0, 19))
        self.label_CPU_3.setMaximumSize(QSize(16777215, 20))
        self.label_CPU_3.setFont(font)
        self.label_CPU_3.setMargin(0)
        self.label_CPU_3.setIndent(0)
        self.label_CPU_4 = QLabel(self.frame)
        self.label_CPU_4.setObjectName(u"label_CPU_4")
        self.label_CPU_4.setGeometry(QRect(210, 0, 161, 19))
        sizePolicy.setHeightForWidth(self.label_CPU_4.sizePolicy().hasHeightForWidth())
        self.label_CPU_4.setSizePolicy(sizePolicy)
        self.label_CPU_4.setMinimumSize(QSize(0, 19))
        self.label_CPU_4.setMaximumSize(QSize(16777215, 20))
        self.label_CPU_4.setFont(font)
        self.label_CPU_4.setMargin(0)
        self.label_CPU_4.setIndent(55)
        self.label_GPU_2 = QLabel(self.frame)
        self.label_GPU_2.setObjectName(u"label_GPU_2")
        self.label_GPU_2.setGeometry(QRect(210, 400, 71, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_2.sizePolicy().hasHeightForWidth())
        self.label_GPU_2.setSizePolicy(sizePolicy)
        self.label_GPU_2.setMinimumSize(QSize(0, 19))
        self.label_GPU_2.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_2.setFont(font)
        self.label_GPU_2.setScaledContents(True)
        self.label_GPU_2.setWordWrap(True)
        self.label_GPU_2.setMargin(0)
        self.label_GPU_2.setIndent(0)
        self.label_GPU_3 = QLabel(self.frame)
        self.label_GPU_3.setObjectName(u"label_GPU_3")
        self.label_GPU_3.setGeometry(QRect(210, 510, 72, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_3.sizePolicy().hasHeightForWidth())
        self.label_GPU_3.setSizePolicy(sizePolicy)
        self.label_GPU_3.setMinimumSize(QSize(0, 19))
        self.label_GPU_3.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_3.setFont(font)
        self.label_GPU_3.setWordWrap(True)
        self.label_GPU_3.setMargin(0)
        self.widget_cuda = roundProgressBar(self.frame)
        self.widget_cuda.setObjectName(u"widget_cuda")
        self.widget_cuda.setGeometry(QRect(290, 470, 71, 61))
        self.widget_cuda.setMaximumSize(QSize(200, 200))
        self.widget_cuda.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_GPU_encode = QLabel(self.frame)
        self.label_GPU_encode.setObjectName(u"label_GPU_encode")
        self.label_GPU_encode.setGeometry(QRect(210, 300, 61, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_encode.sizePolicy().hasHeightForWidth())
        self.label_GPU_encode.setSizePolicy(sizePolicy)
        self.label_GPU_encode.setMinimumSize(QSize(0, 19))
        self.label_GPU_encode.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_encode.setFont(font)
        self.label_GPU_encode.setWordWrap(True)
        self.label_GPU_encode.setMargin(0)
        self.label_GPU_encode.setIndent(0)
        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(-10, 10, 381, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.label_GPU_8 = QLabel(self.frame)
        self.label_GPU_8.setObjectName(u"label_GPU_8")
        self.label_GPU_8.setGeometry(QRect(220, 620, 72, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_8.sizePolicy().hasHeightForWidth())
        self.label_GPU_8.setSizePolicy(sizePolicy)
        self.label_GPU_8.setMinimumSize(QSize(0, 19))
        self.label_GPU_8.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_8.setFont(font)
        self.label_GPU_8.setWordWrap(True)
        self.label_GPU_8.setMargin(0)
        self.widget_Memory = roundProgressBar(self.frame)
        self.widget_Memory.setObjectName(u"widget_Memory")
        self.widget_Memory.setGeometry(QRect(290, 590, 71, 51))
        self.widget_Memory.setMaximumSize(QSize(200, 200))
        self.widget_Memory.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.widget_GPU_DECODE = roundProgressBar(self.frame)
        self.widget_GPU_DECODE.setObjectName(u"widget_GPU_DECODE")
        self.widget_GPU_DECODE.setGeometry(QRect(290, 270, 71, 51))
        self.widget_GPU_DECODE.setMaximumSize(QSize(200, 200))
        self.widget_GPU_DECODE.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_GPU_encode_2 = QLabel(self.frame)
        self.label_GPU_encode_2.setObjectName(u"label_GPU_encode_2")
        self.label_GPU_encode_2.setGeometry(QRect(210, 100, 81, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_encode_2.sizePolicy().hasHeightForWidth())
        self.label_GPU_encode_2.setSizePolicy(sizePolicy)
        self.label_GPU_encode_2.setMinimumSize(QSize(0, 19))
        self.label_GPU_encode_2.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_encode_2.setFont(font)
        self.label_GPU_encode_2.setWordWrap(True)
        self.label_GPU_encode_2.setMargin(0)
        self.label_GPU_encode_2.setIndent(0)
        self.widget_gpu_temperature = roundProgressBar(self.frame)
        self.widget_gpu_temperature.setObjectName(u"widget_gpu_temperature")
        self.widget_gpu_temperature.setGeometry(QRect(290, 70, 71, 51))
        self.widget_gpu_temperature.setMaximumSize(QSize(200, 200))
        self.widget_gpu_temperature.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_GPU_encode_3 = QLabel(self.frame)
        self.label_GPU_encode_3.setObjectName(u"label_GPU_encode_3")
        self.label_GPU_encode_3.setGeometry(QRect(210, 200, 61, 20))
        sizePolicy.setHeightForWidth(self.label_GPU_encode_3.sizePolicy().hasHeightForWidth())
        self.label_GPU_encode_3.setSizePolicy(sizePolicy)
        self.label_GPU_encode_3.setMinimumSize(QSize(0, 19))
        self.label_GPU_encode_3.setMaximumSize(QSize(16777215, 20))
        self.label_GPU_encode_3.setFont(font)
        self.label_GPU_encode_3.setWordWrap(True)
        self.label_GPU_encode_3.setMargin(0)
        self.label_GPU_encode_3.setIndent(0)
        self.widget_GPU_encode = roundProgressBar(self.frame)
        self.widget_GPU_encode.setObjectName(u"widget_GPU_encode")
        self.widget_GPU_encode.setGeometry(QRect(290, 170, 71, 51))
        self.widget_GPU_encode.setMaximumSize(QSize(200, 200))
        self.widget_GPU_encode.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_CPU_5 = QLabel(self.frame)
        self.label_CPU_5.setObjectName(u"label_CPU_5")
        self.label_CPU_5.setGeometry(QRect(390, 0, 161, 19))
        sizePolicy.setHeightForWidth(self.label_CPU_5.sizePolicy().hasHeightForWidth())
        self.label_CPU_5.setSizePolicy(sizePolicy)
        self.label_CPU_5.setMinimumSize(QSize(0, 19))
        self.label_CPU_5.setMaximumSize(QSize(16777215, 20))
        self.label_CPU_5.setFont(font)
        self.label_CPU_5.setMargin(0)
        self.label_CPU_5.setIndent(55)
        self.line_9 = QFrame(self.frame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(380, 10, 201, 20))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.widget_cpu_2 = roundProgressBar(self.frame)
        self.widget_cpu_2.setObjectName(u"widget_cpu_2")
        self.widget_cpu_2.setGeometry(QRect(70, 280, 111, 91))
        self.widget_cpu_2.setMaximumSize(QSize(200, 200))
        self.widget_cpu_2.setStyleSheet(u"/* Central Widget */\n"
"QWidget {\n"
"    background-color: #1d1275;\n"
"}\n"
"")
        self.label_CPU_6 = QLabel(self.frame)
        self.label_CPU_6.setObjectName(u"label_CPU_6")
        self.label_CPU_6.setGeometry(QRect(10, 130, 71, 20))
        sizePolicy1.setHeightForWidth(self.label_CPU_6.sizePolicy().hasHeightForWidth())
        self.label_CPU_6.setSizePolicy(sizePolicy1)
        self.label_CPU_6.setMinimumSize(QSize(0, 19))
        self.label_CPU_6.setMaximumSize(QSize(16777215, 20))
        self.label_CPU_6.setFont(font)
        self.label_CPU_6.setWordWrap(True)
        self.label_CPU_6.setMargin(0)
        self.label_CPU_6.setIndent(0)
        self.label_RAM_2 = QLabel(self.frame)
        self.label_RAM_2.setObjectName(u"label_RAM_2")
        self.label_RAM_2.setGeometry(QRect(420, 130, 91, 28))
        sizePolicy.setHeightForWidth(self.label_RAM_2.sizePolicy().hasHeightForWidth())
        self.label_RAM_2.setSizePolicy(sizePolicy)
        self.label_RAM_2.setMinimumSize(QSize(0, 28))
        self.label_RAM_2.setMaximumSize(QSize(16777215, 27))
        self.label_RAM_2.setFont(font1)
        self.label_RAM_2.setWordWrap(True)
        self.label_RAM_2.setMargin(0)
        self.label_RAM_2.setIndent(0)
        self.label_CPU.raise_()
        self.widget_cpu.raise_()
        self.widget_ram.raise_()
        self.label_RAM.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_GPU.raise_()
        self.widget_gpu.raise_()
        self.label_CPU_3.raise_()
        self.label_GPU_2.raise_()
        self.label_GPU_3.raise_()
        self.widget_cuda.raise_()
        self.label_GPU_encode.raise_()
        self.label_GPU_8.raise_()
        self.widget_Memory.raise_()
        self.widget_GPU_DECODE.raise_()
        self.label_GPU_encode_2.raise_()
        self.widget_gpu_temperature.raise_()
        self.label_GPU_encode_3.raise_()
        self.widget_GPU_encode.raise_()
        self.line_9.raise_()
        self.label_CPU_5.raise_()
        self.line_8.raise_()
        self.label_CPU_2.raise_()
        self.widget_cpu_2.raise_()
        self.label_CPU_6.raise_()
        self.label_RAM_2.raise_()
        self.label_CPU_4.raise_()

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.myStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.myStackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.myStackedWidget, 1, 1, 2, 1)

        self.menu_widget = QCustomSlideMenu(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        sizePolicy.setHeightForWidth(self.menu_widget.sizePolicy().hasHeightForWidth())
        self.menu_widget.setSizePolicy(sizePolicy)
        self.menu_widget.setMinimumSize(QSize(42, 0))
        self.menu_widget.setMaximumSize(QSize(42, 16777215))
        self.verticalLayout = QVBoxLayout(self.menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page1ss = QPushButton(self.menu_widget)
        self.page1ss.setObjectName(u"page1ss")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page1ss.sizePolicy().hasHeightForWidth())
        self.page1ss.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page1ss.setIcon(icon)

        self.verticalLayout.addWidget(self.page1ss)

        self.page2ssss = QPushButton(self.menu_widget)
        self.page2ssss.setObjectName(u"page2ssss")
        sizePolicy2.setHeightForWidth(self.page2ssss.sizePolicy().hasHeightForWidth())
        self.page2ssss.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/network_check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page2ssss.setIcon(icon1)

        self.verticalLayout.addWidget(self.page2ssss)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.menu_widget, 2, 0, 1, 1)

        self.open_close_side_bar_btn = QPushButton(self.centralwidget)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.open_close_side_bar_btn.sizePolicy().hasHeightForWidth())
        self.open_close_side_bar_btn.setSizePolicy(sizePolicy3)
        self.open_close_side_bar_btn.setMinimumSize(QSize(35, 0))
        self.open_close_side_bar_btn.setMaximumSize(QSize(35, 16777215))

        self.gridLayout.addWidget(self.open_close_side_bar_btn, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.myStackedWidget.raise_()
        self.menu_widget.raise_()
        self.open_close_side_bar_btn.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_CPU.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.label_RAM.setText(QCoreApplication.translate("MainWindow", u"Total RAM:", None))
        self.label_GPU.setText(QCoreApplication.translate("MainWindow", u"GPU:", None))
        self.label_CPU_2.setText(QCoreApplication.translate("MainWindow", u"CPU INFO:", None))
        self.label_CPU_3.setText(QCoreApplication.translate("MainWindow", u"Cores:", None))
        self.label_CPU_4.setText(QCoreApplication.translate("MainWindow", u"GPU INFO:", None))
        self.label_GPU_2.setText(QCoreApplication.translate("MainWindow", u"GPU UTILIZATION:", None))
        self.label_GPU_3.setText(QCoreApplication.translate("MainWindow", u"CUDA UTILIZATION:", None))
        self.label_GPU_encode.setText(QCoreApplication.translate("MainWindow", u"VIDEO DECODE:", None))
        self.label_GPU_8.setText(QCoreApplication.translate("MainWindow", u"MEMORY UTILIZATION:", None))
        self.label_GPU_encode_2.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE:", None))
        self.label_GPU_encode_3.setText(QCoreApplication.translate("MainWindow", u"VIDEO ENCODE:", None))
        self.label_CPU_5.setText(QCoreApplication.translate("MainWindow", u"GPU INFO:", None))
        self.label_CPU_6.setText(QCoreApplication.translate("MainWindow", u"CPU UTILIZATION:", None))
        self.label_RAM_2.setText(QCoreApplication.translate("MainWindow", u"RAM UTILIZATION:", None))
        self.page1ss.setText("")
        self.page2ssss.setText("")
        self.open_close_side_bar_btn.setText("")
    # retranslateUi

