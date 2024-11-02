from random import randint, uniform
import sqlite3


class MyMath:
    def generate_square_x(self):
        """
        Вернет кв уравнение в строковом формате.
        """
        a_sq = randint(-3, 5)
        if a_sq == 0:
            while a_sq == 0:
                a_sq = randint(-3, 5)
        b_sq = randint(-9, 9)
        c_sq = randint(-9, 9)
        if b_sq == 0:
            b_sq = 1
        elif c_sq == 0:
            c_sq = 1

        if b_sq == 1:
            if c_sq < 0 and a_sq != 1 and a_sq != -1:
                return f'{a_sq}x\u00B2 + x - {-c_sq} = 0'
            elif c_sq < 0 and a_sq == -1:
                return f'-x\u00B2 + x - {-c_sq} = 0'
            elif c_sq < 0 and a_sq == 1:
                return f'x\u00B2 + x - {-c_sq} = 0'
            elif c_sq > 0 and a_sq != 1 and a_sq != -1:
                return f'{a_sq}x\u00B2 + x + {c_sq} = 0'
            elif c_sq > 0 and a_sq == -1:
                return f'-x\u00B2 + x + {c_sq} = 0'
            elif c_sq > 0 and a_sq == 1:
                return f'x\u00B2 + x + {c_sq} = 0'

        elif b_sq == -1:
            if c_sq < 0 and a_sq != 1 and a_sq != -1:
                return f'{a_sq}x\u00B2 - x - {-c_sq} = 0'
            elif c_sq < 0 and a_sq == -1:
                return f'-x\u00B2 - x - {-c_sq} = 0'
            elif c_sq < 0 and a_sq == 1:
                return f'x\u00B2 - x - {-self.c_sq} = 0'
            elif c_sq > 0 and a_sq != 1 and a_sq != -1:
                return f'{a_sq}x\u00B2 - x + {c_sq} = 0'
            elif c_sq > 0 and a_sq == -1:
                return f'-x\u00B2 - x + {c_sq} = 0'
            elif c_sq > 0 and a_sq == 1:
                return f'x\u00B2 - x + {c_sq} = 0'

        else:
            if b_sq > 0:
                if c_sq < 0 and a_sq != 1 and a_sq != -1:
                    return f'{a_sq}x\u00B2 + {b_sq}x - {-c_sq} = 0'
                elif c_sq < 0 and a_sq == -1:
                    return f'-x\u00B2 + {b_sq}x - {-c_sq} = 0'
                elif c_sq < 0 and a_sq == 1:
                    return f'x\u00B2 + {b_sq}x - {-c_sq} = 0'
                elif c_sq > 0 and a_sq != 1 and b_sq != -1:
                    return f'{a_sq}x\u00B2 + {b_sq}x + {c_sq} = 0'
                elif c_sq > 0 and a_sq == -1:
                    return f'-x\u00B2 + {b_sq}x + {c_sq} = 0'
                elif c_sq > 0 and a_sq == 1:
                    return f'x\u00B2 + {b_sq}x + {c_sq} = 0'
            elif b_sq < 0:
                if c_sq < 0 and a_sq != 1 and a_sq != -1:
                    return f'{a_sq}x\u00B2 - {-b_sq}x - {-c_sq} = 0'
                elif c_sq < 0 and a_sq == -1:
                    return f'-x\u00B2 - {-b_sq}x - {-c_sq} = 0'
                elif c_sq < 0 and a_sq == 1:
                    return f'x\u00B2 - {-b_sq}x - {-c_sq} = 0'
                elif c_sq > 0 and a_sq != 1 and a_sq != -1:
                    return f'{a_sq}x\u00B2 - {-b_sq}x + {c_sq} = 0'
                elif c_sq > 0 and a_sq == -1:
                    return f'-x\u00B2 - {-b_sq}x + {c_sq} = 0'
                elif c_sq > 0 and a_sq == 1:
                    return f'x\u00B2 - {-b_sq}x + {c_sq} = 0'

    def answer_square_x(self, square_x):
        """
        Вернет 1) если дискриминант положительный - список из 2 целых или дробных чисел
                  2) если дискриминант 0 - одно целое или дробное число
                  3) если дискриминант отрицательный - строку "Корней нет"
           корни последнего сгенерированного кв уравнения
           """
        coofs = []
        if square_x.startswith('-'):
            a_sq = -1
        elif square_x.startswith('x'):
            a_sq = 1
        else:
            for i in square_x:
                if i != '\u00B2' and i.isdigit() and int(i) != 0:
                    coofs.append(i)
            a_sq = int(coofs[0])

        square_x = square_x.split()
        if square_x[1] == '-' and square_x[2] == 'x':
            b_sq = -1
        elif square_x[1] == '+' and square_x[2] == 'x':
            b_sq = 1
        else:
            if square_x[1] == '-':
                b_sq = -int(square_x[2][0])
            elif square_x[1] == '+':
                b_sq = int(square_x[2][0])

        if square_x[3] == '-':
            c_sq = -int(square_x[4])
        elif square_x[3] == '+':
            c_sq = int(square_x[4])

        d = (abs(b_sq) ** 2) - (4 * a_sq * c_sq)
        if d == 0:
            answer = (-b_sq) / (2 * a_sq)
            return int(answer)

        elif d > 0:
            x1 = (-b_sq - d ** 0.5) / (2 * a_sq)
            x2 = (-b_sq + d ** 0.5) / (2 * a_sq)
            if int(x1) == x1 and isinstance(x2, float):
                answer = sorted([int(x1), round(x2, 2)])
            elif int(x2) == x2 and isinstance(x1, float):
                answer = sorted([round(x1, 2), int(x2)])
            elif int(x1) == x1 and int(x2) == x2:
                answer = sorted([int(x1), int(x2)])
            elif isinstance(x1, float) and isinstance(x2, float):
                answer = sorted([round(x1, 2), round(x2, 2)])
            return answer

        else:
            answer = 'Корней нет'
            return answer

    def check_answer_square_x(self, task, user_answer):
        """
        В качестве ответа может быть принято
        1) 2 корня кв уравнения через пробел(это могут быть целые числа или дробные(округлите до сотых) числа)
        2) один корень - целое чило или дробное(округлите до сотых) число
        3) строка 'Корней нет'
        """
        if user_answer == 'Корней нет':
            if str(self.answer_square_x(task)) == user_answer:
                return 'Верно'
            else:
                return f'Неверно. Правильный ответ {self.answer_square_x(task)}.'

        elif isinstance(user_answer, int) or isinstance(user_answer, float):
            if float(user_answer) == float(self.answer_square_x(task)):
                return 'Верно'
            else:
                return f'Неверно. Правильный ответ {self.answer_square_x(task)}.'

        temp = [float(i) for i in user_answer.split(' ')]
        if sorted(temp) == list(self.answer_square_x(task)):
            return ['Верно', True, 'square_x']
        else:
            return [f'Неверно. Правильный ответ {self.answer_square_x(task)}.', False]

    def generate_line_x(self):
        """
        Вернет линейное уравнение в строковом формате
        """
        a_li = randint(-9, 9)
        if a_li == 0:
            a_li = 1
        b_li = randint(-9, 9)
        c_li = randint(-9, 9)
        if c_li == 0:
            c_li = 1

        if b_li < 0:
            line_x = f'{a_li}x - {-b_li} = {c_li}'
        elif b_li > 0:
            line_x = f'{a_li}x + {b_li} = {c_li}'
        elif b_li == 0:
            b_li = 1
            line_x = f'{a_li}x + {b_li} = {c_li}'

        if a_li == 1:
            line_x = line_x[1:]
        elif a_li == -1:
            line_x = f'-{line_x[2:]}'
        return line_x

    def answer_line_x(self, line_x):
        """
        Вернет корень последнего сгенерированного линейного уравнения
        """
        line_x = line_x.split()
        if line_x[0][0] == '-' and line_x[0][1] == 'x':
            a_li = -1
        elif line_x[0] == 'x':
            a_li = 1
        else:
            if line_x[0][0] == '-':
                a_li = -int(line_x[0][1])
            else:
                a_li = int(line_x[0][0])

        if line_x[1] == '-':
            b_li = -int(line_x[2])
        elif line_x[1] == '+':
            b_li = int(line_x[2])

        c_li = int(line_x[-1])

        temp_x = c_li + (-b_li)
        if temp_x / a_li == temp_x // a_li:
            x = int(temp_x / a_li)
        else:
            x = round(temp_x / a_li, 2)
        return x

    def check_answer_line_x(self, task, user_answer):
        """
        В качестве ответа может быть принято
        целое число или дробное(округлите до сотых) число
        """
        if float(user_answer) == float(self.answer_line_x(task)):
            return ['Верно', True, 'line_x']
        else:
            return [f'Неверно. Правильный ответ {self.answer_line_x(task)}.', False]

    def search_coofs_for_stage_1_2(self, task):
        """
        Находит коэффициенты примеров простого и среднего уровня сложности.
        """
        task = task.split()
        coofs = [float(task[0]), float(task[2])]
        return coofs

    def search_coofs_for_stage_3(self, task):
        """
        Находит коэффициенты примеров сложного уровня сложности.
        """
        task = task.split()
        coofs = [int(task[0]), float(task[2]), float(task[4]), int(task[6])]
        return coofs

    def answer_for_all_stages(self, task):
        """
        Находит решение на любой пример всех сложностей.
        """
        task = task.split()
        stage = 0

        if len(task) == 5:
            try:
                task[0] = int(task[0])
                task[2] = int(task[2])
                stage = 1
                task[0] = str(task[0])
                task[2] = str(task[2])
            except ValueError:
                pass
            try:
                task[0] = float(task[0])
                task[2] = float(task[2])
                stage = 2
                task[0] = str(task[0])
                task[2] = str(task[2])
            except ValueError:
                pass
        elif len(task) == 9:
            stage = 3

        if task[1] == '+':
            task = ' '.join(task)
            if stage == 1:
                a, b = self.search_coofs_for_stage_1_2(task)
                return a + b
            elif stage == 2:
                a, b = self.search_coofs_for_stage_1_2(task)
                return round(a + b, 2)
            elif stage == 3:
                a, b, c, d = self.search_coofs_for_stage_3(task)
                return round(a + b + c + d, 2)
        elif task[1] == '-':
            task = ' '.join(task)
            if stage == 1:
                a, b = self.search_coofs_for_stage_1_2(task)
                return a - b
            elif stage == 2:
                a, b = self.search_coofs_for_stage_1_2(task)
                return round(a - b, 2)
            elif stage == 3:
                a, b, c, d = self.search_coofs_for_stage_3(task)
                return round(a - b - c - d, 2)
        elif task[1] == ':':
            task = ' '.join(task)
            if stage == 1:
                a, b = self.search_coofs_for_stage_1_2(task)
                return a / b
            elif stage == 2:
                a, b = self.search_coofs_for_stage_1_2(task)
                return round(a / b, 2)
            elif stage == 3:
                a, b, c, d = self.search_coofs_for_stage_3(task)
                return round(a / b / c / d, 2)
        elif task[1] == '*':
            task = ' '.join(task)
            if stage == 1:
                a, b = self.search_coofs_for_stage_1_2(task)
                return a * b
            elif stage == 2:
                a, b = self.search_coofs_for_stage_1_2(task)
                return round(a * b, 2)
            elif stage == 3:
                a, b, c, d = self.search_coofs_for_stage_3(task)
                return round(a * b * c * d, 2)

    def generate_sum_stage_1(self):
        """
        Вернет пример на сложение простого уровня сложности в строковом формате
        """
        a_s_1 = randint(1, 101)
        b_s_1 = randint(1, 101)
        return f'{a_s_1} + {b_s_1} = ?'

    def check_answer_sum_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на сложение простого уровня сложности
        """
        if float(self.answer_for_all_stages(task)) == float(user_answer):
            return ['Верно', True, 's_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_sum_stage_2(self):
        """
        Вернет пример на сложение среднего уровня сложности в строковом формате
        """
        a_s_2 = round(uniform(1, 20), 2)
        b_s_2 = round(uniform(1, 20), 2)
        return f'{a_s_2} + {b_s_2} = ?'

    def check_answer_sum_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на последний сгенерированный пример на сложение среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 's_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_sum_stage_3(self):
        """
        Вернет пример на сложение высокого уровня сложности в строковом формате
        """
        a_s_3 = randint(1, 30)
        b_s_3 = round(uniform(1, 30), 2)
        c_s_3 = round(uniform(1, 30), 2)
        d_s_3 = randint(1, 30)
        return f'{a_s_3} + {b_s_3} + {c_s_3} + {d_s_3} = ?'

    def check_answer_sum_stage_3(self, task, user_answer):
        """
        Проверил ответ пользователя на пример на сложение высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 's_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_min_stage_1(self):
        """
        Вернет пример на вычитание простого уровня сложности в строковом формате
        """
        a_m_1 = randint(1, 101)
        b_m_1 = randint(1, 101)
        return f'{a_m_1} - {b_m_1} = ?'

    def check_answer_min_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание простого уровня сложности
        """
        if float(self.answer_for_all_stages(task)) == float(user_answer):
            return ['Верно', True, 'm_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_min_stage_2(self):
        """
        Вернет пример на вычитание среднего уровня сложности в строковом формате
        """
        a_m_2 = round(uniform(1, 20), 2)
        b_m_2 = round(uniform(1, 20), 2)
        return f'{a_m_2} - {b_m_2} = ?'

    def check_answer_min_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'm_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}', False]

    def generate_min_stage_3(self):
        """
        Вернет пример на вычитание высокого уровня сложности в строковом формате
        """
        a_m_3 = randint(50, 100)
        b_m_3 = round(uniform(30, 50), 2)
        c_m_3 = round(uniform(20, 30), 2)
        d_m_3 = randint(1, 20)
        return f'{a_m_3} - {b_m_3} - {c_m_3} - {d_m_3} = ?'

    def check_answer_min_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'm_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_crop_stage_1(self):
        """
        Вернет пример на деление в строковом формате
        """
        a_cr_1 = randint(1, 51)
        b_cr_1 = randint(1, 51)
        return f'{a_cr_1} : {b_cr_1} = ?'

    def check_answer_crop_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление простого уровня сложности
        """
        if float(self.answer_for_all_stages(task)) == float(user_answer):
            return ['Верно', True, 'cr_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_crop_stage_2(self):
        """
        Вернет пример на деление среднего уровня сложности в строковом формате
        """
        a_cr_2 = round(uniform(1, 20), 2)
        b_cr_2 = round(uniform(1, 20), 2)
        return f'{a_cr_2} : {b_cr_2} = ?'

    def check_answer_crop_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'cr_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_crop_stage_3(self):
        """
        Вернет пример на деление высокого уровня сложности в строковом формате
        """
        a_cr_3 = randint(50, 100)
        b_cr_3 = round(uniform(30, 50), 2)
        c_cr_3 = round(uniform(20, 30), 2)
        d_cr_3 = randint(1, 20)
        return f'{a_cr_3} : {b_cr_3} : {c_cr_3} : {d_cr_3} = ?'

    def check_answer_crop_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'cr_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}', False]

    def generate_multiply_stage_1(self):
        """
        Вернет пример на умножение в строковом формате
        """
        a_mul_1 = randint(1, 21)
        b_mul_1 = randint(1, 21)
        return f'{a_mul_1} * {b_mul_1} = ?'

    def check_answer_multiply_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение простого уровня сложности
        """
        if float(self.answer_for_all_stages(task)) == float(user_answer):
            return ['Верно', True, 'mul_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}.', False]

    def generate_multiply_stage_2(self):
        """
        Вернет пример на умножение среднего уровня сложности в строковом формате
        """
        a_mul_2 = round(uniform(1, 10), 2)
        b_mul_2 = round(uniform(1, 10), 2)
        return f'{a_mul_2} * {b_mul_2} = ?'

    def check_answer_multiply_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'mul_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}', False]

    def generate_multiply_stage_3(self):
        """
        Вернет пример на умножение высокого уровня сложности в строковом формате
        """
        a_mul_3 = randint(1, 10)
        b_mul_3 = round(uniform(1, 10), 2)
        c_mul_3 = round(uniform(1, 10), 2)
        d_mul_3 = randint(1, 10)
        return f'{a_mul_3} * {b_mul_3} * {c_mul_3} * {d_mul_3} = ?'

    def check_answer_multiply_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_for_all_stages(task)):
            return ['Верно', True, 'mul_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_for_all_stages(task)}', False]

    def create_easy_test(self):
        self.creater = MyMath()
        self.task1 = self.creater.generate_square_x()
        self.task2 = self.creater.generate_line_x()
        self.task3 = self.creater.generate_sum_stage_1()
        self.task4 = self.creater.generate_min_stage_1()
        self.task5 = self.creater.generate_multiply_stage_1()
        self.task6 = self.creater.generate_crop_stage_1()
        self.task_list = [self.task1, self.task2, self.task3, self.task4, self.task5, self.task6]
        return self.task_list

    def answer_easy_test(self, task_list):
        answers = []
        ans1 = self.answer_square_x(task_list[0])
        answers.append(ans1)
        ans2 = self.answer_line_x(task_list[1])
        answers.append(ans2)
        for task in task_list[2:]:
            ans = self.answer_for_all_stages(task)
            answers.append(ans)
        return answers

    def create_hard_test(self):
        self.creater = MyMath()
        self.task1_1 = self.creater.generate_square_x()
        self.task2_1 = self.creater.generate_line_x()
        self.task3_1 = self.creater.generate_sum_stage_2()
        self.task4_1 = self.creater.generate_sum_stage_3()
        self.task5_1 = self.creater.generate_min_stage_2()
        self.task6_1 = self.creater.generate_min_stage_3()
        self.task7_1 = self.creater.generate_multiply_stage_2()
        self.task8_1 = self.creater.generate_multiply_stage_3()
        self.task9_1 = self.creater.generate_crop_stage_2()
        self.task10_1 = self.creater.generate_crop_stage_3()
        self.task_list_1 = [self.task1_1, self.task2_1, self.task3_1, self.task4_1, self.task5_1,
                            self.task6_1, self.task7_1, self.task8_1, self.task9_1, self.task10_1]
        return self.task_list_1

    def answer_hard_test(self, task_list):
        answers_1 = []
        ans1_1 = self.answer_square_x(task_list[0])
        answers_1.append(ans1_1)
        ans2_1 = self.answer_line_x(task_list[1])
        answers_1.append(ans2_1)
        for task in task_list[2:]:
            ans_1 = self.answer_for_all_stages(task)
            answers_1.append(ans_1)
        return answers_1

    def edit_rating_tasks(self, login, true_task):
        data_tasks = {'square_x': 15, 'line_x': 10, 's_1': 3, 's_2': 5, 's_3': 10,
                      'm_1': 3, 'm_2': 5, 'm_3': 10, 'cr_1': 3, 'cr_2': 5,
                      'cr_3': 10, 'mul_1': 3, 'mul_2': 5, 'mul_3': 10}
        point = data_tasks[true_task]
        con = sqlite3.connect('project_db.sqlite')
        cursor = con.cursor()
        points = cursor.execute(f'''SELECT points FROM stats WHERE login="{login}"''').fetchone()
        if not points:
            points = point
        else:
            points = point + points[0]
        cursor.execute(f'''UPDATE stats SET points={points} WHERE login="{login}"''')
        con.commit()
        con.close()
        return point
