from PyQt6 import QtCore, QtGui, QtWidgets


class TestOpenWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 463)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(226, 110, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 591, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 661, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 280, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.start_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(300, 330, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.exit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(284, 360, 101, 23))
        self.exit_btn.setObjectName("exit_btn")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 180, 471, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест"))
        self.label.setText(_translate("MainWindow", "Легкий тест."))
        self.label_2.setText(_translate("MainWindow", "Тест состоит из 6 заданий."))
        self.label_3.setText(_translate("MainWindow", "Вы можете давать и изменять ответ неограниченное количество раз на любое задание,  "))
        self.label_4.setText(_translate("MainWindow", "В каждой строке для ответа нужно ввести ответ в соответствии с правилами."))
        self.label_5.setText(_translate("MainWindow", "Правила формата ответа на каждое задание будут указаны на странице этого задания."))
        self.label_6.setText(_translate("MainWindow", "Удачи!!!"))
        self.start_btn.setText(_translate("MainWindow", "Начать"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти в меню"))
        self.label_7.setText(_translate("MainWindow", "но если вы завершите тест, то ответы нельзя будет изменить."))