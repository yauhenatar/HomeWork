# Задачи ООП

# задача 1

class Student():

    def __init__(self, name, potions, mag_hist, herb, transf):
        self.name = name
        self.grade = potions + mag_hist + herb + transf

    def exam_grade(self):
        return print(f'Оценка {self.name} за экзамен ', self.grade)

#задача 2

from datetime import datetime as dt

class GreatTalent():

    def __init__(self, name, age, fav_prog_lang):
        self.name = name
        self.age = age
        self.fav_prog_lang = fav_prog_lang

    def year_of_birth(self):
        return print(dt.now().year - self.age)

# задача 3

class Horse():

    population = 0

    def __init__(self, hooves, color, breed, name, jockey):
        self.hooves = hooves
        self.color = color
        self.breed = breed
        self.name = name
        self.jockey = jockey
        Horse.population += 1

    def nicker(self):
        print(f'{self.name} восклицает: "И-го-го"')

    def hop(self):
        from random import randint
        return print(f'{self.name} скачет со скоростью {randint(15, 89)} км/ч')

    def eat(self):
        print(f'{self.name} видит яблоко и кушает его')

# задача 4

class Jockey(Horse):

    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

    def ride(self):
        self.hop()

# ООП инкапсуляция и полиморфия

# задача 1

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self):

        email = input('Введите новый email: ')

        if email.count('@') == 1 and email.count('.') > 0 and email.rfind('.') > email.find('@'):

            self.__email = email

        else:

            return print('Ошибочная почта')

# задача 2

class Robot:

    def __init__(self, name, birth_year, mental, physical):
        self.name = name
        self.birth_year = birth_year
        self.__mental = mental
        self.__physical = physical

    def get_condition(self):

        cond_info = round(self.__physical + self.__mental, 4)

        if cond_info <= -1:
            return print('Я чувствую себя несчастным!')

        elif -1 < cond_info <= 0:
            return print('Я чувствую себя плохо!')

        elif 0 < cond_info <= 0.5:
            return print('Могло быть хуже!')

        elif 0.5 < cond_info <= 1:
            return print('Кажется, всё в порядке!')

        else:
            return print('Супер!')

# задача 3

class Money:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.total_cents = (dollars * 100) + cents

    def get_dollars(self):
        return self.dollars

    def set_dollars(self, dollars):

        if type(dollars) == int and dollars >= 0:
            self.total_cents = dollars * 100

        else:

            print('Error dollars')

    def get_cents(self):
        return self.cents

    def set_cents(self, cents):

        if type(cents) == int and 0 <= cents < 100:
            self.total_cents = cents

        else:

            print('Error cents')

    def __str__(self):
        return print(f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов')


# задача 4

class Player:

    colours = ['red', 'green', 'blue']

    def __init__(self, nick, role='undefined', colour='undefined'):
        self.nick = nick
        self.role = role
        self.colour = colour

    def set_color(self):

        if Player.colours:

            if self.colour == 'undefined':

                print('Выберите цвет: ', *Player.colours)
                colour = input('Введите цвет: ')
                self.colour = colour
                Player.colours.remove(colour)
                print('Выбран цвет: ', colour, '\n')


        else:

            print('Цвет не может быть назначен! Очередь уже заполнена :(')

# ООП классы, объекты, наследования

# задача 1

class ReactAngle:

    def __init__(self, first_len=10, second_len=5):
        self.first_len = first_len
        self.second_len = second_len

    def calculate_area(self):
        return print('Площадь = ', self.first_len * self.second_len)

    def draw(self):
        return print(('*' * self.first_len + '\n') * self.second_len)

# задача 2

class Square(ReactAngle):

    def __int__(self, length=3):
        self.length = length

# задача 3

class Elevator:

    def __init__(self, sum_floor=5, cur_floor=3):
        self.sum_floor = sum_floor
        self.cur_floor = cur_floor

    def up_button(self):
        if self.cur_floor == self.sum_floor:
            return print('Лифт не может подняться выше')
        else:
            self.cur_floor = self.cur_floor + 1
            return  print(f'Лифт поднимается на {self.cur_floor} этаж')

    def down_button(self):
        if self.cur_floor <= 1:
            return print('Лифт не может опуститься ниже')
        else:
            self.cur_floor = self.cur_floor - 1
            return print(f'Лифт опускается на {self.cur_floor} этаж')

# задача 4

class NewElevator(Elevator):

    def __init__(self, sum_floor, cur_floor):
        super().__init__(sum_floor, cur_floor)

    def move(self, floor):
        if floor in range(1, self.sum_floor + 1):
            return print(f'Лифт отправляется с {self.cur_floor} этажа на {floor} этаж')
        else:
            return print('Неправильный номер этажа')