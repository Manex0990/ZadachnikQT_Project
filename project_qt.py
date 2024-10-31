from project import MyMath
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('zadachnik_menu.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())


# square_x_btn
# line_x_btn
# sum_btn
# min_btn
# mul_btn
# crop_btn
# easy_test_btn
# hard_test_btn
# добавить картинки
