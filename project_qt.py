from project import MyMath
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Titul_list(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('zadachnik.ui', self)
        self.start_btn.clicked.connect(self.test_window)

    def test_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Titul_list()
    ex.show()
    sys.exit(app.exec())
