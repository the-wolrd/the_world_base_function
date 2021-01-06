# -*- coding: utf-8 -*-

################################################################################
# QT Designer 를 구글링해서 알아보세요.
# Googleing QT Designer
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 200)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 4px solid rgb(255, 0, 0);\n"
"	font: 16pt \"777\ubd09\uc22d\uc544\ud2f4\ud2b8\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(23, 23, 23);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 4px solid rgb(0, 255, 0);\n"
"	font: 16pt \"777\ubd09\uc22d\uc544\ud2f4\ud2b8\";\n"
"}\n"
"\n"
"QPushButton:hover::pressed{\n"
"	background-color: rgb(38, 38, 38);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 4px solid rgb(0, 0, 255);\n"
"	font: 16pt \"777\ubd09\uc22d\uc544\ud2f4\ud2b8\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(50, 30))

        self.horizontalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.btn1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"btn", None))
    # retranslateUi

