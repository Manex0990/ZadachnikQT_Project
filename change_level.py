from PyQt6 import QtCore, QtGui, QtWidgets


class ChangeLevelWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 271)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 241, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.easy_btn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.easy_btn.setGeometry(QtCore.QRect(40, 70, 82, 17))
        self.easy_btn.setObjectName("easy_btn")
        self.medium_btn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.medium_btn.setGeometry(QtCore.QRect(40, 110, 82, 17))
        self.medium_btn.setObjectName("medium_btn")
        self.hard_btn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.hard_btn.setGeometry(QtCore.QRect(40, 150, 82, 17))
        self.hard_btn.setObjectName("hard_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор уровня сложности"))
        self.label.setText(_translate("MainWindow", "Выбирете уровень сложности примера"))
        self.easy_btn.setText(_translate("MainWindow", "Легкий"))
        self.medium_btn.setText(_translate("MainWindow", "Средний"))
        self.hard_btn.setText(_translate("MainWindow", "Сложный"))
