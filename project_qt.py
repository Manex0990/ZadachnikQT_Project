from project import MyMath
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup


class Task(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag1 = None
        uic.loadUi('task_doing.ui', self)
        self.task = MyMath.generate_square_x(self)
        self.taskLine.setText(self.task)
        self.answer_btn.clicked.connect(self.check_task)
        self.exit_btn.clicked.connect(self.exit)

    def check_task(self):
        user_answer = self.answerLine.text()
        try:
            user_answer = float(user_answer)
        except ValueError:
            pass
        if user_answer != 'Корней нет' and not isinstance(user_answer, float) and \
                not isinstance(user_answer.split(), list):
            self.statusBar().showMessage('Неверный формат ответа.')
        else:
            if user_answer == 'Корней нет':
                pass
            else:
                user_answer = list(map(float, user_answer.split()))
            verdict = MyMath.check_answer_square_x(self, self.task, user_answer)
            if verdict[1]:
                self.verdictLine.setText(verdict[0])
                corr = verdict[2]
            else:
                self.verdictLine.setText(verdict[0])

    def exit(self):
        if self.flag1 is None:
            self.flag1 = Menu()
        self.flag1.show()
        self.hide()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = None
        uic.loadUi('zadachnik_menu.ui', self)
        self.training_tasks_btn_group = QButtonGroup(self)
        self.training_tasks_btn_group.addButton(self.square_x_btn)
        self.training_tasks_btn_group.addButton(self.line_x_btn)
        self.training_tasks_btn_group.addButton(self.sum_btn)
        self.training_tasks_btn_group.addButton(self.min_btn)
        self.training_tasks_btn_group.addButton(self.mul_btn)
        self.training_tasks_btn_group.addButton(self.crop_btn)
        self.training_tasks_btn_group.buttonClicked.connect(self.open_task_window)

    def open_task_window(self):
        if self.flag is None:
            self.flag = Task()
        self.flag.show()
        self.hide()


app = QApplication(sys.argv)
w = Menu()
w.show()
app.exec()
