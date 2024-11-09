from project import MyMath
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup


class LevelChangeWindow(QMainWindow):
    def __init__(self, btn):
        super().__init__()
        self.stage = 0
        self.btn = btn
        self.flag = None
        uic.loadUi('change_level.ui', self)
        self.levels = QButtonGroup(self)
        self.levels.addButton(self.easy_btn)
        self.levels.addButton(self.medium_btn)
        self.levels.addButton(self.hard_btn)
        self.levels.buttonClicked.connect(self.change_and_open)

    def change_and_open(self):
        if self.easy_btn.isChecked():
            self.stage = 1
        elif self.medium_btn.isChecked():
            self.stage = 2
        else:
            self.stage = 3
        if self.flag is None:
            self.flag = Task(self.btn, self.stage)
        self.flag.show()
        self.hide()


class Task(QMainWindow):
    def __init__(self, btn, level=0):
        super().__init__()
        self.flag1 = None
        self.flag2 = None
        self.btn = btn
        self.stage = level
        if self.btn == 'Квадратное уравнение':
            uic.loadUi('task_doing.ui', self)
            self.task = MyMath.generate_square_x(self)
            self.answer_btn.clicked.connect(self.check_task_square_x)
        elif self.btn == 'Линейное уравнение':
            uic.loadUi('task_doing_1.ui', self)
            self.task = MyMath.generate_line_x(self)
            self.answer_btn.clicked.connect(self.check_task_line_x)
        elif self.btn == 'Пример на сложение':
            uic.loadUi('task_doing_2.ui', self)
            self.label.setText('Задание Пример на сложение')
            self.label_2.setText('Задача: Решите пример на сложение.')
            if self.stage == 1:
                self.task = MyMath.generate_sum_stage_1(self)
            elif self.stage == 2:
                self.task = MyMath.generate_sum_stage_2(self)
            else:
                self.task = MyMath.generate_sum_stage_3(self)
            self.answer_btn.clicked.connect(self.check_task_all_stages)
        elif self.btn == 'Пример на вычитание':
            uic.loadUi('task_doing_2.ui', self)
            self.label.setText('Задание Пример на вычитание')
            self.label_2.setText('Задача: Решите пример на вычитание.')
            if self.stage == 1:
                self.task = MyMath.generate_min_stage_1(self)
            elif self.stage == 2:
                self.task = MyMath.generate_min_stage_2(self)
            else:
                self.task = MyMath.generate_min_stage_3(self)
            self.answer_btn.clicked.connect(self.check_task_all_stages)
        elif self.btn == 'Пример на умножение':
            uic.loadUi('task_doing_2.ui', self)
            self.label.setText('Задание Пример на умножение')
            self.label_2.setText('Задача: Решите пример на умножение.')
            if self.stage == 1:
                self.task = MyMath.generate_multiply_stage_1(self)
            elif self.stage == 2:
                self.task = MyMath.generate_multiply_stage_2(self)
            else:
                self.task = MyMath.generate_multiply_stage_3(self)
            self.answer_btn.clicked.connect(self.check_task_all_stages)
        elif self.btn == 'Пример на деление':
            uic.loadUi('task_doing_2.ui', self)
            self.label.setText('Задание Пример на деление')
            self.label_2.setText('Задача: Решите пример на деление.')
            if self.stage == 1:
                self.task = MyMath.generate_crop_stage_1(self)
            elif self.stage == 2:
                self.task = MyMath.generate_crop_stage_2(self)
            else:
                self.task = MyMath.generate_crop_stage_3(self)
            self.answer_btn.clicked.connect(self.check_task_all_stages)
        self.taskLine.setText(self.task)
        self.exit_btn.clicked.connect(self.exit)

    def check_task_square_x(self):
        user_answer = self.answerLine.text()
        if user_answer == 'Корней нет':
            verdict = MyMath.check_answer_square_x(self, self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            if verdict[1]:
                corr = verdict[2]
        elif user_answer.isalnum():
            verdict = MyMath.check_answer_square_x(self, self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            if verdict[1]:
                corr = verdict[2]
        else:
            try:
                user_answer = user_answer.split()
                user_answer = sorted(list(map(float, user_answer)))
                verdict = MyMath.check_answer_square_x(self, self.task, user_answer)
                self.verdictLine.setText(verdict[0])
                if verdict[1]:
                    corr = verdict[2]
            except ValueError:
                self.statusBar().showMessage('Неверный формат ответа.')
            except TypeError:
                self.statusBar().showMessage('Неверный формат ответа.')

    def check_task_line_x(self):
        user_answer = self.answerLine.text()
        try:
            user_answer = float(user_answer)
            verdict = MyMath.check_answer_line_x(self, self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            if verdict[1]:
                corr = verdict[2]
            else:
                pass
        except ValueError:
            self.statusBar().showMessage('Неверный формат ответа.')
        except TypeError:
            self.statusBar().showMessage('Неверный формат ответа.')

    def check_task_all_stages(self):
        user_answer = self.answerLine.text()
        try:
            user_answer = float(user_answer)
            verdict = MyMath.check_answer_for_all_stages(self, self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            if verdict[1]:
                corr = verdict[2]
            else:
                pass
        except ValueError:
            self.statusBar().showMessage('Неверный формат ответа.')
        except TypeError:
            self.statusBar().showMessage('Неверный формат ответа.')

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

    def open_task_window(self, button):
        name = button.text()
        if self.flag is None and (name == 'Квадратное уравнение' or name == 'Линейное уравнение'):
            self.flag = Task(name)
        elif self.flag is None and 'Пример' in name:
            self.flag = LevelChangeWindow(name)
        self.flag.show()
        self.hide()


app = QApplication(sys.argv)
w = Menu()
w.show()
app.exec()
