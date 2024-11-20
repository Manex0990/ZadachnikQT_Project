from PyQt6 import QtCore, QtGui, QtWidgets


class TestDoingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 572)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tasksTabs = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tasksTabs.setGeometry(QtCore.QRect(0, 0, 841, 481))
        self.tasksTabs.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tasksTabs.setUsesScrollButtons(True)
        self.tasksTabs.setTabsClosable(False)
        self.tasksTabs.setMovable(False)
        self.tasksTabs.setTabBarAutoHide(False)
        self.tasksTabs.setObjectName("tasksTabs")
        self.end_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.end_btn.setGeometry(QtCore.QRect(740, 480, 101, 31))
        self.end_btn.setObjectName("end_btn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 490, 571, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tasksTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Легкий тест"))
        self.end_btn.setText(_translate("MainWindow", "Завершить тест"))
        self.label.setText(_translate("MainWindow", "Если вы завершите тест, то не сможете изменять ответы."))
