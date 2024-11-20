from project import MyMath
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
import sqlite3
from zadachnik_menu import MenuWindow
from task_doing import TaskWindow
from test_doing import TestOpenWindow
from easy_test_doing import TestDoingWindow
from change_level import ChangeLevelWindow


class LevelChangeWindow(QMainWindow, ChangeLevelWindow):
    def __init__(self, btn):
        super().__init__()
        self.setupUi(self)
        self.stage = 0
        self.btn = btn
        self.open_task = None
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
        if self.open_task is None:
            self.open_task = Task(self.btn, self.stage)
        self.open_task.show()
        self.hide()


class Task(QMainWindow, TaskWindow):
    def __init__(self, btn, level=0, test=None):
        super().__init__()
        self.ex = MyMath()
        self.main_window_open = None
        self.counter = 0
        self.btn = btn
        self.stage = level
        self.test = test
        self.methods_with_levels = {
            'Квадратное уравнение': ('Задание Квадратное уравнение', 'Задача: Решите квадратное уравнение.',
                                     'square_x', {0: self.ex.generate_square_x},
                                     self.check_task_square_x),
            'Линейное уравнение': ('Задание Линейное уравнение', 'Задача: Решите линейное уравнение.',
                                   'other_task', {0: self.ex.generate_line_x},
                                   self.check_task_all_stages_and_line_x),
            'Пример на сложение': ('Задание Пример на сложение', 'Задача: Решите пример на сложение.',
                                   'other_task', {1: self.ex.generate_sum_stage_1,
                                                                      2: self.ex.generate_sum_stage_2,
                                                                      3: self.ex.generate_sum_stage_3},
                                   self.check_task_all_stages_and_line_x),
            'Пример на вычитание': ('Задание Пример на вычитание', 'Задача: Решите пример на вычитание.',
                                    'other_task', {1: self.ex.generate_min_stage_1,
                                                                       2: self.ex.generate_min_stage_2,
                                                                       3: self.ex.generate_min_stage_3},
                                    self.check_task_all_stages_and_line_x),
            'Пример на умножение': ('Задание Пример на умножение', 'Задача: Решите пример на умножение.',
                                    'other_task', {1: self.ex.generate_multiply_stage_1,
                                                                       2: self.ex.generate_multiply_stage_2,
                                                                       3: self.ex.generate_multiply_stage_3},
                                    self.check_task_all_stages_and_line_x),
            'Пример на деление': ('Задание Пример на деление', 'Задача: Решите пример на деление.',
                                  'other_task', {1: self.ex.generate_crop_stage_1,
                                                                     2: self.ex.generate_crop_stage_2,
                                                                     3: self.ex.generate_crop_stage_3},
                                  self.check_task_all_stages_and_line_x)}
        self.create_task_type(self.methods_with_levels[self.btn])

    def create_task_type(self, generate_methods):
        text1, text2, ui_file, method, check_method = generate_methods
        method = method[self.stage]
        self.setupUi(self, ui_file)
        self.label.setText(text1)
        self.label_2.setText(text2)
        self.task = method()
        self.answer_btn.clicked.connect(check_method)
        self.taskLine.setText(self.task)
        self.exit_btn.clicked.connect(self.exit)

    def check_task_square_x(self):
        user_answer = self.answerLine.text()
        if user_answer == 'Корней нет':
            verdict = self.ex.check_answer_square_x(self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            self.flagLine.setText('Принято')
            if verdict[1] and self.counter == 0:
                self.corr = verdict[2]
                if self.test is None:
                    self.edit_rating(1)
                else:
                    self.edit_rating(2)
        elif user_answer.isalnum():
            verdict = self.ex.check_answer_square_x(self.task, user_answer)
            self.verdictLine.setText(verdict[0])
            self.flagLine.setText('Принято')
            if verdict[1] and self.counter == 0:
                self.corr = verdict[2]
                if self.test is None:
                    self.edit_rating(1)
                else:
                    self.edit_rating(2)
        else:
            try:
                user_answer = user_answer.split()
                user_answer = sorted(list(map(float, user_answer)))
                verdict = self.ex.check_answer_square_x(self.task, user_answer)
                self.verdictLine.setText(verdict[0])
                self.flagLine.setText('Принято')
                if verdict[1] and self.counter == 0:
                    self.corr = verdict[2]
                    if self.test is None:
                        self.edit_rating(1)
                    else:
                        self.edit_rating(2)
            except ValueError:
                self.statusBar().showMessage('Неверный формат ответа.')
                self.verdictLine.setText('Неверно')
                self.flagLine.setText('Принято')
            except TypeError:
                self.statusBar().showMessage('Неверный формат ответа.')
                self.verdictLine.setText('Неверно')
                self.flagLine.setText('Принято')

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
            if verdict[1] and self.counter == 0:
                self.corr = verdict[2]
                if self.test is None:
                    self.edit_rating(1)
                else:
                    self.edit_rating(2)
            else:
                pass
        except ValueError:
            self.statusBar().showMessage('Неверный формат ответа.')
            self.verdictLine.setText('Неверно')
            self.flagLine.setText('Принято')
        except TypeError:
            self.statusBar().showMessage('Неверный формат ответа.')
            self.verdictLine.setText('Неверно')
            self.flagLine.setText('Принято')

    def edit_rating(self, cof):
        self.counter = 1
        con = sqlite3.connect('rating_db.sqlite')
        cur = con.cursor()
        query = f'''SELECT point FROM points WHERE tilte = "{self.corr}"'''
        temp = cur.execute(query).fetchone()
        temp = temp[0]
        temp = temp * cof
        query = f'''UPDATE main SET rating = rating + "{temp}" WHERE id = "YOU"'''
        cur.execute(query)
        con.commit()
        con.close()

    def exit(self):
        if self.main_window_open is None:
            self.main_window_open = Menu()
        self.main_window_open.show()
        self.hide()


class OpenTest(QMainWindow, TestOpenWindow):
    def __init__(self, btn):
        super().__init__()
        self.setupUi(self)
        self.ex = MyMath()
        self.open_test_window = None
        self.open_main_window = None
        if btn == 'Легкий тест':
            self.level = 1
        elif btn == 'Сложный тест':
            self.level = 2
            self.label.setText(btn)
            self.label_2.setText('Тест состоит из 10 заданий.')
        self.start_btn.clicked.connect(self.test)
        self.exit_btn.clicked.connect(self.exit)

    def test(self):
        if self.open_test_window is None:
            self.open_test_window = Test(self.level)
        self.open_test_window.show()
        self.hide()

    def exit(self):
        if self.open_main_window is None:
            self.open_main_window = Menu()
        self.open_main_window.show()
        self.hide()


class Test(QMainWindow, TestDoingWindow):
    def __init__(self, level):
        super().__init__()
        self.setupUi(self)
        self.open_main_window = None
        self.level = level
        if self.level == 1:
            self.data = [Task('Квадратное уравнение', test=self), Task('Линейное уравнение', test=self),
                         Task('Пример на сложение', level=1, test=self),
                         Task('Пример на вычитание', level=1, test=self),
                         Task('Пример на умножение', level=1, test=self),
                         Task('Пример на деление', level=1, test=self)]
        elif self.level == 2:
            self.data = [Task('Квадратное уравнение', test=self), Task('Линейное уравнение', test=self),
                         Task('Пример на сложение', level=2, test=self),
                         Task('Пример на сложение', level=3, test=self),
                         Task('Пример на вычитание', level=2, test=self),
                         Task('Пример на вычитание', level=3, test=self),
                         Task('Пример на умножение', level=2, test=self),
                         Task('Пример на умножение', level=3, test=self),
                         Task('Пример на деление', level=2, test=self),
                         Task('Пример на деление', level=3, test=self)]
        for i in range(len(self.data)):
            self.tasksTabs.addTab(self.data[i], str(i + 1))
        for i in range(len(self.data)):
            self.data[i].verdictLine.hide()
            self.data[i].exit_btn.hide()
        self.end_btn.clicked.connect(self.exit)

    def exit(self):
        if self.open_main_window is None:
            self.open_main_window = Menu()
        self.open_main_window.show()
        self.hide()


class Menu(QMainWindow, MenuWindow):
    def __init__(self):
        super().__init__()
        self.open_task = None
        self.setupUi(self)
        self.setStyleSheet('background-image: url("background.jpg")')
        self.update_rating()
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

    def update_rating(self):
        con = sqlite3.connect('rating_db.sqlite')
        cur = con.cursor()
        query = '''SELECT rating FROM main WHERE id = "YOU"'''
        rating = cur.execute(query).fetchone()
        self.rating.display(rating[0])
        con.close()

    def open_task_window(self, button):
        name = button.text()
        if self.open_task is None and (name == 'Квадратное уравнение' or name == 'Линейное уравнение'):
            self.open_task = Task(name)
        if self.open_task is None and 'Пример' in name:
            self.open_task = LevelChangeWindow(name)
        self.open_task.show()
        self.hide()

    def open_test_window(self, button):
        name = button.text()
        if self.open_task is None:
            self.open_task = OpenTest(name)
        self.open_task.show()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    w = Menu()
    w.show()
    app.exec()
