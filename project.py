from random import randint, uniform
import sqlite3


class MyMath:
    def generate_square_x(self):
        """
        Вернет кв уравнение в строковом формате.
        """
        self.a_sq = randint(-3, 5)
        if self.a_sq == 0:
            while self.a_sq == 0:
                self.a_sq = randint(-3, 5)
        self.b_sq = randint(-9, 9)
        self.c_sq = randint(-9, 9)
        if self.b_sq == 0:
            self.b_sq = 1
        elif self.c_sq == 0:
            self.c_sq = 1

        if self.b_sq == 1:
            if self.c_sq < 0 and self.a_sq != 1 and self.a_sq != -1:
                return f'{self.a_sq}x\u00B2 + x - {-self.c_sq} = 0'
            elif self.c_sq < 0 and self.a_sq == -1:
                return f'-x\u00B2 + x - {-self.c_sq} = 0'
            elif self.c_sq < 0 and self.a_sq == 1:
                return f'x\u00B2 + x - {-self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq != 1 and self.a_sq != -1:
                return f'{self.a_sq}x\u00B2 + x + {self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq == -1:
                return f'-x\u00B2 + x + {self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq == 1:
                return f'x\u00B2 + x + {self.c_sq} = 0'

        elif self.b_sq == -1:
            if self.c_sq < 0 and self.a_sq != 1 and self.a_sq != -1:
                return f'{self.a_sq}x\u00B2 - x - {-self.c_sq} = 0'
            elif self.c_sq < 0 and self.a_sq == -1:
                return f'-x\u00B2 - x - {-self.c_sq} = 0'
            elif self.c_sq < 0 and self.a_sq == 1:
                return f'x\u00B2 - x - {-self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq != 1 and self.a_sq != -1:
                return f'{self.a_sq}x\u00B2 - x + {self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq == -1:
                return f'-x\u00B2 - x + {self.c_sq} = 0'
            elif self.c_sq > 0 and self.a_sq == 1:
                return f'x\u00B2 - x + {self.c_sq} = 0'

        else:
            if self.b_sq > 0:
                if self.c_sq < 0 and self.a_sq != 1 and self.a_sq != -1:
                    return f'{self.a_sq}x\u00B2 + {self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq < 0 and self.a_sq == -1:
                    return f'-x\u00B2 + {self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq < 0 and self.a_sq == 1:
                    return f'x\u00B2 + {self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq != 1 and self.b_sq != -1:
                    return f'{self.a_sq}x\u00B2 + {self.b_sq}x + {self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq == -1:
                    return f'-x\u00B2 + {self.b_sq}x + {self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq == 1:
                    return f'x\u00B2 + {self.b_sq}x + {self.c_sq} = 0'
            elif self.b_sq < 0:
                if self.c_sq < 0 and self.a_sq != 1 and self.a_sq != -1:
                    return f'{self.a_sq}x\u00B2 - {-self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq < 0 and self.a_sq == -1:
                    return f'-x\u00B2 - {-self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq < 0 and self.a_sq == 1:
                    return f'x\u00B2 - {-self.b_sq}x - {-self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq != 1 and self.a_sq != -1:
                    return f'{self.a_sq}x\u00B2 - {-self.b_sq}x + {self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq == -1:
                    return f'-x\u00B2 - {-self.b_sq}x + {self.c_sq} = 0'
                elif self.c_sq > 0 and self.a_sq == 1:
                    return f'x\u00B2 - {-self.b_sq}x + {self.c_sq} = 0'

    def answer_square_x(self, square_x):
        """
        Вернет 1) если дискриминант положительный - список из 2 целых или дробных чисел
                  2) если дискриминант 0 - одно целое или дробное число
                  3) если дискриминант отрицательный - строку "Корней нет"
           корни последнего сгенерированного кв уравнения
           """
        coofs = []
        if square_x.startswith('-'):
            self.a_sq = -1
        elif square_x.startswith('x'):
            self.a_sq = 1
        else:
            for i in square_x:
                if i != '\u00B2' and i.isdigit() and int(i) != 0:
                    coofs.append(i)
            self.a_sq = int(coofs[0])

        square_x = square_x.split()
        if square_x[1] == '-' and square_x[2] == 'x':
            self.b_sq = -1
        elif square_x[1] == '+' and square_x[2] == 'x':
            self.b_sq = 1
        else:
            if square_x[1] == '-':
                self.b_sq = -int(square_x[2][0])
            elif square_x[1] == '+':
                self.b_sq = int(square_x[2][0])

        if square_x[3] == '-':
            self.c_sq = -int(square_x[4])
        elif square_x[3] == '+':
            self.c_sq = int(square_x[4])

        d = (abs(self.b_sq) ** 2) - (4 * self.a_sq * self.c_sq)
        if d == 0:
            self.answer = (-self.b_sq) / (2 * self.a_sq)
            return int(self.answer)

        elif d > 0:
            x1 = (-self.b_sq - d ** 0.5) / (2 * self.a_sq)
            x2 = (-self.b_sq + d ** 0.5) / (2 * self.a_sq)
            if int(x1) == x1 and isinstance(x2, float):
                self.answer = sorted([int(x1), round(x2, 2)])
            elif int(x2) == x2 and isinstance(x1, float):
                self.answer = sorted([round(x1, 2), int(x2)])
            elif int(x1) == x1 and int(x2) == x2:
                self.answer = sorted([int(x1), int(x2)])
            elif isinstance(x1, float) and isinstance(x2, float):
                self.answer = sorted([round(x1, 2), round(x2, 2)])
            return self.answer

        else:
            self.answer = 'Корней нет'
            return self.answer

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
        self.a_li = randint(-9, 9)
        self.b_li = randint(-9, 9)
        self.c_li = randint(-9, 9)

        if self.b_li < 0:
            line_x = f'{self.a_li}x - {-self.b_li} = {self.c_li}'
        elif self.b_li > 0:
            line_x = f'{self.a_li}x + {self.b_li} = {self.c_li}'
        elif self.b_li == 0:
            self.b_li = 1
            line_x = f'{self.a_li}x + {self.b_li} = {self.c_li}'

        if self.a_li == 1 or self.a_li == 0:
            self.a_li = 1
            line_x = line_x[1:]
        elif self.a_li == -1:
            line_x = f'-{line_x[2:]}'
        return line_x

    def answer_line_x(self, line_x):
        """
        Вернет корень последнего сгенерированного линейного уравнения
        """
        line_x = line_x.split()
        if line_x[0][0] == '-' and line_x[0][1] == 'x':
            self.a_li = -1
        elif line_x[0] == 'x':
            self.a_li = 1
        else:
            if line_x[0][0] == '-':
                self.a_li = -int(line_x[0][1])
            else:
                self.a_li = int(line_x[0][0])

        if line_x[1] == '-':
            self.b_li = -int(line_x[2])
        elif line_x[1] == '+':
            self.b_li = int(line_x[2])

        self.c_li = int(line_x[-1])

        temp_x = self.c_li + (-self.b_li)
        if temp_x / self.a_li == temp_x // self.a_li:
            self.x = temp_x // self.a_li
        else:
            self.x = round(temp_x / self.a_li, 2)
        return self.x

    def check_answer_line_x(self, task, user_answer):
        """
        В качестве ответа может быть принято
        целое число или дробное(округлите до сотых) число
        """
        if float(user_answer) == float(self.answer_line_x(task)):
            return ['Верно', True, 'line_x']
        else:
            return [f'Неверно. Правильный ответ {self.answer_line_x(task)}.', False]

    def generate_sum_stage_1(self):
        """
        Вернет пример на сложение простого уровня сложности в строковом формате
        """
        self.a_s_1 = randint(1, 101)
        self.b_s_1 = randint(1, 101)
        return f'{self.a_s_1} + {self.b_s_1} = ?'

    def answer_sum_stage_1(self, sum_1):
        """
        Вернет решение последнего сгенерированного примера на сложение простого уровня сложности
        """
        sum_1 = sum_1.split()
        self.a_s_1 = int(sum_1[0])
        self.b_s_1 = int(sum_1[2])
        return self.a_s_1 + self.b_s_1

    def check_answer_sum_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на сложение простого уровня сложности
        """
        if float(self.answer_sum_stage_1(task)) == float(user_answer):
            return ['Верно', True, 's_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_sum_stage_1(task)}.', False]

    def generate_sum_stage_2(self):
        """
        Вернет пример на сложение среднего уровня сложности в строковом формате
        """
        self.a_s_2 = round(uniform(1, 20), 2)
        self.b_s_2 = round(uniform(1, 20), 2)
        return f'{self.a_s_2} + {self.b_s_2} = ?'

    def answer_sum_stage_2(self, sum_2):
        """
        Вернет ответ на последний сгенерированный пример на сложение среднего уровня сложности
        """
        sum_2 = sum_2.split()
        self.a_s_2 = float(sum_2[0])
        self.b_s_2 = float(sum_2[2])
        return self.a_s_2 + self.b_s_2

    def check_answer_sum_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на последний сгенерированный пример на сложение среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_sum_stage_2(task)):
            return ['Верно', True, 's_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_sum_stage_2(task)}.', False]

    def generate_sum_stage_3(self):
        """
        Вернет пример на сложение высокого уровня сложности в строковом формате
        """
        self.a_s_3 = randint(1, 30)
        self.b_s_3 = round(uniform(1, 30), 2)
        self.c_s_3 = round(uniform(1, 30), 2)
        self.d_s_3 = randint(1, 30)
        return f'{self.a_s_3} + {self.b_s_3} + {self.c_s_3} + {self.d_s_3} = ?'

    def answer_sum_stage_3(self, sum_3):
        """
        Вернет ответ на последний сгенерированный пример на сложение высокого уровня сложности
        """
        sum_3 = sum_3.split()
        self.a_s_3 = int(sum_3[0])
        self.b_s_3 = float(sum_3[2])
        self.c_s_3 = float(sum_3[4])
        self.d_s_3 = int(sum_3[6])
        return round(self.a_s_3 + self.b_s_3 + self.c_s_3 + self.d_s_3, 2)

    def check_answer_sum_stage_3(self, task, user_answer):
        """
        Проверил ответ пользователя на пример на сложение высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_sum_stage_3(task)):
            return ['Верно', True, 's_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_sum_stage_3(task)}.', False]

    def generate_min_stage_1(self):
        """
        Вернет пример на вычитание простого уровня сложности в строковом формате
        """
        self.a_m_1 = randint(1, 101)
        self.b_m_1 = randint(1, 101)
        return f'{self.a_m_1} - {self.b_m_1} = ?'

    def answer_min_stage_1(self, min_1):
        """
        Вернет решение последнего сгенерированного примера на вычитание простого уровня сложности
        """
        min_1 = min_1.split()
        self.a_m_1 = int(min_1[0])
        self.b_m_1 = int(min_1[2])
        return self.a_m_1 - self.b_m_1

    def check_answer_min_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание простого уровня сложности
        """
        if float(self.answer_min_stage_1(task)) == float(user_answer):
            return ['Верно', True, 'm_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_min_stage_1(task)}.', False]

    def generate_min_stage_2(self):
        """
        Вернет пример на вычитание среднего уровня сложности в строковом формате
        """
        self.a_m_2 = round(uniform(1, 20), 2)
        self.b_m_2 = round(uniform(1, 20), 2)
        return f'{self.a_m_2} - {self.b_m_2} = ?'

    def answer_min_stage_2(self, min_2):
        """
        Вернет ответ на последний сгенерированный пример на вычитание среднего уровня сложности
        """
        min_2 = min_2.split()
        self.a_m_2 = float(min_2[0])
        self.b_m_2 = float(min_2[2])
        return round(self.a_m_2 - self.b_m_2, 2)

    def check_answer_min_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_min_stage_2(task)):
            return ['Верно', True, 'm_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_min_stage_2(task)}', False]

    def generate_min_stage_3(self):
        """
        Вернет пример на вычитание высокого уровня сложности в строковом формате
        """
        self.a_m_3 = randint(1, 30)
        self.b_m_3 = round(uniform(1, 30), 2)
        self.c_m_3 = round(uniform(1, 30), 2)
        self.d_m_3 = randint(1, 30)
        return f'{self.a_m_3} - {self.b_m_3} - {self.c_m_3} - {self.d_m_3} = ?'

    def answer_min_stage_3(self, min_3):
        """
        Вернет ответ на последний сгенерированный пример на вычитание высокого уровня сложности
        """
        min_3 = min_3.split()
        self.a_m_3 = int(min_3[0])
        self.b_m_3 = float(min_3[2])
        self.c_m_3 = float(min_3[4])
        self.d_m_3 = int(min_3[6])
        return round(self.a_m_3 - self.b_m_3 - self.c_m_3 - self.d_m_3, 2)

    def check_answer_min_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на вычитание высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_min_stage_3(task)):
            return ['Верно', True, 'm_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_min_stage_3(task)}.', False]

    def generate_crop_stage_1(self):
        """
        Вернет пример на деление в строковом формате
        """
        self.a_cr_1 = randint(1, 51)
        self.b_cr_1 = randint(1, 51)
        return f'{self.a_cr_1} : {self.b_cr_1} = ?'

    def answer_crop_stage_1(self, crop_1):
        """
        Вернет решение последнего сгенерированного примера на деление
        """
        crop_1 = crop_1.split()
        self.a_cr_1 = int(crop_1[0])
        self.b_cr_1 = int(crop_1[2])
        if self.a_cr_1 / self.b_cr_1 == self.a_cr_1 // self.b_cr_1:
            return self.a_cr_1 // self.b_cr_1
        else:
            return round(self.a_cr_1 / self.b_cr_1, 2)

    def check_answer_crop_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление простого уровня сложности
        """
        if float(self.answer_crop_stage_1(task)) == float(user_answer):
            return ['Верно', True, 'cr_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_crop_stage_1(task)}.', False]

    def generate_crop_stage_2(self):
        """
        Вернет пример на деление среднего уровня сложности в строковом формате
        """
        self.a_cr_2 = round(uniform(1, 20), 2)
        self.b_cr_2 = round(uniform(1, 20), 2)
        return f'{self.a_cr_2} : {self.b_cr_2} = ?'

    def answer_crop_stage_2(self, crop_2):
        """
        Вернет ответ на последний сгенерированный пример на деление среднего уровня сложности
        """
        crop_2 = crop_2.split()
        self.a_cr_2 = float(crop_2[0])
        self.b_cr_2 = float(crop_2[2])
        return round(self.a_cr_2 / self.b_cr_2, 2)

    def check_answer_crop_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_crop_stage_2(task)):
            return ['Верно', True, 'cr_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_crop_stage_2(task)}.', False]

    def generate_crop_stage_3(self):
        """
        Вернет пример на деление высокого уровня сложности в строковом формате
        """
        self.a_cr_3 = randint(1, 30)
        self.b_cr_3 = round(uniform(1, 30), 2)
        self.c_cr_3 = round(uniform(1, 30), 2)
        self.d_cr_3 = randint(1, 30)
        return f'{self.a_cr_3} : {self.b_cr_3} : {self.c_cr_3} : {self.d_cr_3} = ?'

    def answer_crop_stage_3(self, crop_3):
        """
        Вернет ответ на последний сгенерированный пример на деление высокого уровня сложности
        """
        crop_3 = crop_3.split()
        self.a_cr_3 = int(crop_3[0])
        self.b_cr_3 = float(crop_3[2])
        self.c_cr_3 = float(crop_3[4])
        self.d_cr_3 = int(crop_3[6])
        temp1 = self.a_cr_3 / self.b_cr_3
        temp2 = self.c_cr_3 / self.d_cr_3
        return round(temp1 / temp2, 2)

    def check_answer_crop_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на деление высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_crop_stage_3(task)):
            return ['Верно', True, 'cr_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_crop_stage_3(task)}', False]

    def generate_multiply_stage_1(self):
        """
        Вернет пример на умножение в строковом формате
        """
        self.a_mul_1 = randint(1, 21)
        self.b_mul_1 = randint(1, 21)
        return f'{self.a_mul_1} * {self.b_mul_1} = ?'

    def answer_multiply_stage_1(self, mul_1):
        """
        Вернет решение последнего сгенерированного примера на умножение
        """
        mul_1 = mul_1.split()
        self.a_mul_1 = int(mul_1[0])
        self.b_mul_1 = int(mul_1[2])
        return self.a_mul_1 * self.b_mul_1

    def check_answer_multiply_stage_1(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение простого уровня сложности
        """
        if float(self.answer_multiply_stage_1(task)) == float(user_answer):
            return ['Верно', True, 'mul_1']
        else:
            return [f'Неверно. Правильный ответ {self.answer_multiply_stage_1(task)}.', False]

    def generate_multiply_stage_2(self):
        """
        Вернет пример на умножение среднего уровня сложности в строковом формате
        """
        self.a_mul_2 = round(uniform(1, 10), 2)
        self.b_mul_2 = round(uniform(1, 10), 2)
        return f'{self.a_mul_2} * {self.b_mul_2} = ?'

    def answer_multiply_stage_2(self, mul_2):
        """
        Вернет ответ на последний сгенерированный пример на умножение среднего уровня сложности
        """
        mul_2 = mul_2.split()
        self.a_mul_2 = float(mul_2[0])
        self.b_mul_2 = float(mul_2[2])
        return round(self.a_mul_2 * self.b_mul_2, 2)

    def check_answer_multiply_stage_2(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение среднего уровня сложности
        """
        if float(user_answer) == float(self.answer_multiply_stage_2(task)):
            return ['Верно', True, 'mul_2']
        else:
            return [f'Неверно. Правильный ответ {self.answer_multiply_stage_2(task)}', False]

    def generate_multiply_stage_3(self):
        """
        Вернет пример на умножение высокого уровня сложности в строковом формате
        """
        self.a_mul_3 = randint(1, 10)
        self.b_mul_3 = round(uniform(1, 10), 2)
        self.c_mul_3 = round(uniform(1, 10), 2)
        self.d_mul_3 = randint(1, 10)
        return f'{self.a_mul_3} * {self.b_mul_3} * {self.c_mul_3} * {self.d_mul_3} = ?'

    def answer_multiply_stage_3(self, mul_3):
        """
        Вернет ответ на последний сгенерированный пример на умножение высокого уровня сложности
        """
        mul_3 = mul_3.split()
        self.a_mul_3 = int(mul_3[0])
        self.b_mul_3 = float(mul_3[2])
        self.c_mul_3 = float(mul_3[4])
        self.d_mul_3 = int(mul_3[6])
        return round(self.a_mul_3 * self.b_mul_3 * self.c_mul_3 * self.d_mul_3, 2)

    def check_answer_multiply_stage_3(self, task, user_answer):
        """
        Проверит ответ пользователя на пример на умножение высокого уровня сложности
        """
        if float(user_answer) == float(self.answer_multiply_stage_3(task)):
            return ['Верно', True, 'mul_3']
        else:
            return [f'Неверно. Правильный ответ {self.answer_multiply_stage_3(task)}', False]

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
        self.ans1 = self.answer_square_x(task_list[0])
        self.ans2 = self.answer_line_x(task_list[1])
        self.ans3 = self.answer_sum_stage_1(task_list[2])
        self.ans4 = self.answer_min_stage_1(task_list[3])
        self.ans5 = self.answer_multiply_stage_1(task_list[4])
        self.ans6 = self.answer_crop_stage_1(task_list[5])
        self.answers = [self.ans1, self.ans2, self.ans3, self.ans4, self.ans5, self.ans6]
        return self.answers

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
        self.ans1_1 = self.answer_square_x(task_list[0])
        self.ans2_1 = self.answer_line_x(task_list[1])
        self.ans3_1 = self.answer_sum_stage_2(task_list[2])
        self.ans4_1 = self.answer_sum_stage_3(task_list[3])
        self.ans5_1 = self.answer_min_stage_2(task_list[4])
        self.ans6_1 = self.answer_min_stage_3(task_list[5])
        self.ans7_1 = self.answer_multiply_stage_2(task_list[6])
        self.ans8_1 = self.answer_multiply_stage_3(task_list[7])
        self.ans9_1 = self.answer_crop_stage_2(task_list[8])
        self.ans10_1 = self.answer_crop_stage_3(task_list[9])
        self.answers_1 = [self.ans1_1, self.ans2_1, self.ans3_1, self.ans4_1, self.ans5_1,
                          self.ans6_1, self.ans7_1, self.ans8_1, self.ans9_1, self.ans10_1]
        return self.answers_1

    def edit_rating_tasks(self, login, true_task):
        data_tasks = {'square_x': 15, 'line_x': 10, 's_1': 3, 's_2': 5, 's_3': 10,
                      'm_1': 3, 'm_2': 5, 'm_3': 10, 'cr_1': 3, 'cr_2': 5,
                      'cr_3': 10, 'mul_1': 3, 'mul_2': 5, 'mul_3': 10}
        point = data_tasks[true_task]
        con = sqlite3.connect('project.db')
        cursor = con.cursor()
        points = cursor.execute(f'''SELECT points FROM stats WHERE login="{login}"''').fetchone()
        if not points:
            points = point
        else:
            points = point + points[0]
        cursor.execute(f'''UPDATE stats SET points={points}  WHERE login="{login}"''')
        con.commit()
        con.close()
        return point

    def edit_rating_tests(self, login, true_test):
        pass
