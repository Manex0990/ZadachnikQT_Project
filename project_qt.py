from project import MyMath
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
import sqlite3


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
        self.ex = MyMath()
        self.flag1 = None
        self.flag2 = None
        self.btn = btn
        self.stage = level
        if self.btn == 'Квадратное уравнение':
            uic.loadUi('task_doing.ui', self)
            self.task = self.ex.generate_square_x()
            self.answer_btn.clicked.connect(self.check_task_square_x)
        else:
            uic.loadUi('task_doing_1.ui', self)
            if self.btn == 'Линейное уравнение':
                self.label.setText('Задание Линейное уравнение')
                self.label_2.setText('Задача: Решите линейное уравнение.')
                self.task = self.ex.generate_line_x()
            elif self.btn == 'Пример на сложение':
                self.label.setText('Задание Пример на сложение')
                self.label_2.setText('Задача: Решите пример на сложение.')
                if self.stage == 1:
                    self.task = self.ex.generate_sum_stage_1()
                elif self.stage == 2:
                    self.task = self.ex.generate_sum_stage_2()
                else:
                    self.task = self.ex.generate_sum_stage_3()
            elif self.btn == 'Пример на вычитание':
                self.label.setText('Задание Пример на вычитание')
                self.label_2.setText('Задача: Решите пример на вычитание.')
                if self.stage == 1:
                    self.task = self.ex.generate_min_stage_1()
                elif self.stage == 2:
                    self.task = self.ex.generate_min_stage_2()
                else:
                    self.task = self.ex.generate_min_stage_3()
            elif self.btn == 'Пример на умножение':
                self.label.setText('Задание Пример на умножение')
                self.label_2.setText('Задача: Решите пример на умножение.')
                if self.stage == 1:
                    self.task = self.ex.generate_multiply_stage_1()
                elif self.stage == 2:
                    self.task = self.ex.generate_multiply_stage_2()
                else:
                    self.task = self.ex.generate_multiply_stage_3()
            elif self.btn == 'Пример на деление':
                self.label.setText('Задание Пример на деление')
                self.label_2.setText('Задача: Решите пример на деление.')
                if self.stage == 1:
                    self.task = self.ex.generate_crop_stage_1()
                elif self.stage == 2:
                    self.task = self.ex.generate_crop_stage_2()
                else:
                    self.task = self.ex.generate_crop_stage_3()
            self.answer_btn.clicked.connect(self.check_task_all_stages_and_line_x)
        self.taskLine.setText(self.task)
        self.exit_btn.clicked.connect(self.exit)

    def check_task_square_x(self):
        user_answer = self.answerLine.text()
        if user_answer == 'Корней нет':
            verdict = self.ex.check_answer_square_x(self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            self.flagLine.setText('Принято')
            if verdict[1]:
                corr = verdict[2]
        elif user_answer.isalnum():
            verdict = self.ex.check_answer_square_x(self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            self.flagLine.setText('Принято')
            if verdict[1]:
                corr = verdict[2]
        else:
            try:
                user_answer = user_answer.split()
                user_answer = sorted(list(map(float, user_answer)))
                verdict = self.ex.check_answer_square_x(self.task, user_answer)
                self.verdictLine.setText(verdict[0])
                self.flagLine.setText('Принято')
                if verdict[1]:
                    corr = verdict[2]
            except ValueError:
                self.statusBar().showMessage('Неверный формат ответа.')
                verdict = 'Неверно'
                self.verdictLine.setText('Неверно')
                self.flagLine.setText('Принято')
            except TypeError:
                self.statusBar().showMessage('Неверный формат ответа.')
                verdict = 'Неверно'
                self.verdictLine.setText('Неверно')
                self.flagLine.setText('Принято')
        return verdict

    def check_task_all_stages_and_line_x(self):
        user_answer = self.answerLine.text()
        try:
            user_answer = float(user_answer)
            if 'x' in self.task:
                verdict = self.ex.check_answer_line_x(self.task, user_answer)
            else:
                verdict = self.ex.check_answer_for_all_stages(self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            self.flagLine.setText('Принято')
            if verdict[1]:
                corr = verdict[2]
                #con = sqlite3.connect('rating_db.sqlite')
                #cur = con.cursor()
                #query = f'''SELECT point FROM points WHERE title = "{corr}"'''
                #temp = cur.execute(query).fetchone()
                #query = f'''UPDATE main SET rating = rating + temp'''
                #cur.execute(query).fetchone()
                #con.commit()
                #con.close()
            else:
                pass
        except ValueError:
            self.statusBar().showMessage('Неверный формат ответа.')
            verdict = 'Неверно'
            self.verdictLine.setText('Неверно')
            self.flagLine.setText('Принято')
        except TypeError:
            self.statusBar().showMessage('Неверный формат ответа.')
            verdict = 'Неверно'
            self.verdictLine.setText('Неверно')
            self.flagLine.setText('Принято')
        return verdict

    def exit(self):
        if self.flag1 is None:
            self.flag1 = Menu()
        self.flag1.show()
        self.hide()


class Open_test(QMainWindow):
    def __init__(self, btn):
        super().__init__()
        self.ex = MyMath()
        self.flag = None
        self.flag1 = None
        uic.loadUi('test_doing.ui', self)
        if btn == 'Легкий тест':
            self.level = 1
        elif btn == 'Сложный тест':
            self.level = 2
            self.label.setText(btn)
            self.label_2.setText('Тест состоит из 10 заданий.')
        self.start_btn.clicked.connect(self.test)
        self.exit_btn.clicked.connect(self.exit)

    def test(self):
        if self.flag1 is None:
            self.flag1 = Test(self.level)
        self.flag1.show()
        self.hide()

    def exit(self):
        if self.flag is None:
            self.flag = Menu()
        self.flag.show()
        self.hide()


class Test(QMainWindow):
    def __init__(self, level):
        super().__init__()
        self.flag = None
        self.level = level
        uic.loadUi('easy_test_doing.ui', self)
        self.tasksTabs.removeTab(0)
        self.tasksTabs.removeTab(1)
        if self.level == 1:
            self.data = [Task('Квадратное уравнение'), Task('Линейное уравнение'),
                         Task('Пример на сложение', level=1), Task('Пример на вычитание', level=1),
                         Task('Пример на умножение', level=1), Task('Пример на деление', level=1)]
            for i in range(len(self.data)):
                self.tasksTabs.addTab(self.data[i], str(i + 1))
            for i in range(len(self.data)):
                self.data[i].verdictLine.hide()
                self.data[i].exit_btn.hide()
        elif self.level == 2:
            self.data = [Task('Квадратное уравнение'), Task('Линейное уравнение'),
                         Task('Пример на сложение', level=2), Task('Пример на сложение', level=3),
                         Task('Пример на вычитание', level=2), Task('Пример на вычитание', level=3),
                         Task('Пример на умножение', level=2), Task('Пример на умножение', level=3),
                         Task('Пример на деление', level=2), Task('Пример на деление', level=3)]
            for i in range(len(self.data)):
                self.tasksTabs.addTab(self.data[i], str(i + 1))
            for i in range(len(self.data)):
                self.data[i].verdictLine.hide()
                self.data[i].exit_btn.hide()
        self.tasksTabs.removeTab(0)
        self.end_btn.clicked.connect(self.exit)

    def exit(self):
        self.verdicts = []
        correct = []
        not_correct = []
        for i in range(len(self.data)):
            if i == 0:
                self.verdicts.append(self.data[i].check_task_square_x())
            else:
                self.verdicts.append(self.data[i].check_task_all_stages_and_line_x())
        for i in self.verdicts:
            if 'Верно' in i[0]:
                correct.append('1')
            elif 'Неверно' in i[0]:
                not_correct.append('0')
        procent_cor = len(correct) // len(self.verdicts)
        if self.flag is None:
            self.flag = Menu()
        self.flag.show()
        self.hide()

        # вызвать метод класса task чтоб вытащить перемнную обновления рейтинга.

        # перенести наружу таба кнопку выхода или передавать обьект test в качестве аргумкента в task
        # тоже самое с кнопкой завершения теста


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = None
        uic.loadUi('zadachnik_menu.ui', self)
        task_buttons = [self.square_x_btn, self.line_x_btn, self.sum_btn, self.min_btn, self.mul_btn, self.crop_btn]
        self.training_tasks_btn_group = QButtonGroup(self)
        for i in task_buttons:
            self.training_tasks_btn_group.addButton(i)
        self.training_tasks_btn_group.buttonClicked.connect(self.open_task_window)
        test_buttons = [self.easy_test_btn, self.hard_test_btn]
        self.training_tests_btn_group = QButtonGroup(self)
        for i in test_buttons:
            self.training_tests_btn_group.addButton(i)
        self.training_tests_btn_group.buttonClicked.connect(self.open_test_window)

    def open_task_window(self, button):
        name = button.text()
        if self.flag is None and (name == 'Квадратное уравнение' or name == 'Линейное уравнение'):
            self.flag = Task(name)
        elif self.flag is None and 'Пример' in name:
            self.flag = LevelChangeWindow(name)
        self.flag.show()
        self.hide()

    def open_test_window(self, button):
        name = button.text()
        if self.flag is None:
            self.flag = Open_test(name)
        self.flag.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Menu()
    w.show()
    app.exec()
