import collections
from datetime import datetime, timedelta
import random

admins = {1 :['admin', 'admin', 'ADMIN'],
          2 :['fenya', 'fenyastar1337', 'Лазюк Валерий Семёнович'],
          3 :['artemiy', 'krutoidizayner4ever', 'Лебедев Артемий Батькович']}

receipt_collection = {1: {'Номер квитанции': '1', 'ФИО владельца техники': 'Никулин', 'Тип изделия': 'телефон', 'Бренд': 'xiaomi', 'Операционная система': 'android', 'Описание поломки': 'треснуло стекло', 'Дата приемки': '03.06.2022', 'Дата выполнения ремонта': '07.06.2022', 'Статус ремонта': 'в ремонте'},
                      2: {'Номер квитанции': '2', 'ФИО владельца техники': 'Дорошко', 'Тип изделия': 'телевизор', 'Бренд': 'samsung', 'Диагональ экрана': '32', 'Описание поломки': 'битый пиксель', 'Дата приемки': '03.06.2022', 'Дата выполнения ремонта': '07.06.2022', 'Статус ремонта': 'в ремонте'},
                      }

# Родительский класс
class Technics:
    def __init__(self):
        self.brand = input('Марка: ')
        self.brake_info = input('Описание поломки: ')


# Дочерние классы (наследуют одинаковые параметры от родителя)
class Phone(Technics):

    def get_info(self):
        self.os = input('Операционная система: ')


class Notebook(Technics):

    def get_info(self):
        self.os = input('Операционная система: ')
        self.issue_year = input('Год выпуска: ')


class TV(Technics):

    def get_info(self):
        self.diagonal = input('Диагональ экрана: ')


class Info:

    def __init__(self):
        self.accept_date = datetime.now().date()
        self.repair_date = self.get_repair_date()
        self.status = 'в ремонте'


    def get_repair_date(self):
        return self.accept_date + timedelta(days=random.randint(1, 5))

    def set_status(self):
        self.status = input('Введите статус ремонта (ремонтируется, отремонтировано, отдано заказчику): ')

class Admin:

    # пропускатель в админку
    @staticmethod
    def login():

        uncorrectLogin = True

        while uncorrectLogin:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            for key, value in admins.items():
                if login == value[0] and password == value[1]:
                    print('\t'f'Добро пожаловать, {value[2]}')
                    uncorrectLogin = False
                    break
            else:
                print('Неправильное имя пользователя или пароль! Попробуйте ещё раз')

    #получатель админов
    @staticmethod
    def get_admins():
        print('Список администраторов (в формате логин, пароль, ФИО админа): ')
        for key, value in admins.items():
            print(admins[key])

    #удалятель админов
    @staticmethod
    def del_admin():
        admToDel = str(input('Введите логин или ФИО админа, которого нужно удалить: '))
        new_admins = admins.copy()
        for key, value in new_admins.items():
            if admToDel in value:
                del admins[key]

    #добавлятель админов
    @staticmethod
    def add_admin():
        new_admin = []
        login = input('Введите логин админа: ')
        password = input('Введите пароль админа: ')
        full_name = input('Введите ФИО админа: ')
        new_admin.append(login)
        new_admin.append(password)
        new_admin.append(full_name)
        neednum = len(admins.keys()) + 1
        admins[neednum] = new_admin


# Чек
class Receipt:
    def __init__(self):
        self._info_core = Info()

    def run(self):

        global prod
        technics_list = ['телефон', 'ноутбук', 'телевизор']
        self.rec_num = 0
        isTechnicsExists = True

        while isTechnicsExists:

            print('\t\nДля входа в админ-панель введите 1'
                  '\t\nДля сдачи техники в ремонт введите 2'
                  '\t\nДля просмотра информацию введите 3'
                  '\t\nДля выхода введите 4')
            num_prog = input('\nВаш выбор: ')

            if int(num_prog) == 1:
                print('\nВойдите в систему')
                Admin.login()

                admFlag = True

                while admFlag:

                    print('\t\nДля просмотра списка всех админов введите 1'
                          '\t\nДля удаления админа введите 2'
                          '\t\nДля добавления нового админа введите 3'
                          '\t\nДля работы с квитанциями введите 4'
                          '\t\nДля возврата в главное меню введите 5')
                    adm_choise = input('\nВаш выбор: ')

                    if int(adm_choise) == 1:
                        Admin.get_admins()

                    elif int(adm_choise) == 2:
                        Admin.del_admin()

                    elif int(adm_choise) == 3:
                        Admin.add_admin()

                    elif int(adm_choise) == 4:

                        recFlag = True

                        while recFlag:

                            rec_num = str(input('\nВведите номер квитанции, с которой желаете работать: '))

                            print('\t\nДля изменения статуса ремонта, введите 1'
                                  '\t\nДля изменения даты ремонта, введите 2'
                                  '\t\nДля просмотра информации о квитанции, введите 3'
                                  '\t\nДля выхода, введите 4')
                            new_choise = input('\nВаш выбор: ')

                            if int(new_choise) == 1:
                                new_status = input('\nВведите новый статус ремонта техники: ')
                                for key in receipt_collection.keys():
                                    for rec, title in receipt_collection[key].items():
                                        if rec_num.isdigit() and int(rec_num) == key:
                                            receipt_collection[key]['Статус ремонта'] = new_status
                                break


                            elif int(new_choise) == 2:
                                new_rep_date = input('\nВведите новую дату ремонта техники: ')
                                for key in receipt_collection.keys():
                                    for rec, title in receipt_collection[key].items():
                                        if rec_num.isdigit() and int(rec_num) == key:
                                            receipt_collection[key]['Дата выполнения ремонта'] = new_rep_date
                                break

                            elif int(new_choise) == 3:

                                infoFlag = True

                                while infoFlag:

                                    # пробегаюсь по ключам верхнего словаря
                                    for key in receipt_collection.keys():
                                        # обращаюсь к внутреннему словарю
                                        for rec, title in receipt_collection[key].items():
                                            # проверяю наличие в соответствующем ключе
                                            if rec_num.isdigit() and int(rec_num) == key:
                                                # вывожу словарь
                                                print(rec, title, sep=': ')

                                    # это для завершения цикла
                                    break

                            elif int(new_choise) == 4:
                                print('Возвращаемся')
                                break

                        else:
                            print('Неверный ввод! Попробуйте ещё раз')

                    elif int(adm_choise) == 5:
                        print('Возвращаемся')
                        break

                    else:
                        print('Неверный ввод! Попробуйте ещё раз')


            elif int(num_prog) == 2:

                self.rec_num = 1 if len(receipt_collection) == 0 else self.rec_num + 1

                self.full_name = input('Введите ваши ФИО: ')
                self.prod_type = input(
                    'Введите тип техники, который сдаёте в ремонт (телефон, ноутбук, телевизор): ').lower()
                if self.prod_type not in technics_list:
                    print('Неправильно введена техника! Попробуйте ещё раз.')
                else:
                    if self.prod_type == 'телефон':
                        prod = Phone()
                    elif self.prod_type == 'ноутбук':
                        prod = Notebook()
                    elif self.prod_type == 'телевизор':
                        prod = TV()

                    prod.get_info()

                    if self.prod_type == 'телефон':
                        total_receipt = {'Номер квитанции':(str(self.rec_num)),
                                        'ФИО владельца техники':(str(self.full_name)),
                                        'Тип изделия':(str(self.prod_type)),
                                        'Бренд':(str(prod.brand)),
                                        'Операционная система':(str(prod.os)),
                                        'Описание поломки':(str(prod.brake_info)),
                                        'Дата приемки':(str(self._info_core.accept_date.strftime('%d.%m.%Y'))),
                                        'Дата выполнения ремонта':(str(self._info_core.repair_date.strftime('%d.%m.%Y'))),
                                        'Статус ремонта':(str(self._info_core.status))}

                    elif self.prod_type == 'ноутбук':
                        total_receipt = {'Номер квитанции': (str(self.rec_num)),
                                        'ФИО владельца техники': (str(self.full_name)),
                                        'Тип изделия': (str(self.prod_type)),
                                        'Бренд': (str(prod.brand)),
                                        'Операционная система': (str(prod.os)),
                                        'Год выпуска':(str(prod.issue_year)),
                                        'Описание поломки': (str(prod.brake_info)),
                                        'Дата приемки': (str(self._info_core.accept_date.strftime('%d.%m.%Y'))),
                                        'Дата выполнения ремонта': (str(self._info_core.repair_date.strftime('%d.%m.%Y'))),
                                        'Статус ремонта': (str(self._info_core.status))}

                    elif self.prod_type == 'телевизор':
                        total_receipt = {'Номер квитанции': (str(self.rec_num)),
                                         'ФИО владельца техники': (str(self.full_name)),
                                         'Тип изделия': (str(self.prod_type)),
                                         'Бренд': (str(prod.brand)),
                                         'Диагональ экрана': (str(prod.diagonal)),
                                         'Описание поломки': (str(prod.brake_info)),
                                         'Дата приемки': (str(self._info_core.accept_date.strftime('%d.%m.%Y'))),
                                         'Дата выполнения ремонта': (str(self._info_core.repair_date.strftime('%d.%m.%Y'))),
                                         'Статус ремонта': (str(self._info_core.status))}


                    receipt_collection.update({self.rec_num: total_receipt})

                    print(total_receipt)

                    oneMoreTime = input('\nХотите продолжить работу? Введите "Да" или "Нет": ').lower()
                    if oneMoreTime != 'да':
                        isTechnicsExists = False

            elif int(num_prog) == 3:

                infoFlag = True

                while infoFlag:
                    name_or_rec = str(input('Введите ФИО или номер квитанции: '))

                    # пробегаюсь по ключам верхнего словаря
                    for key in receipt_collection.keys():
                        # обращаюсь к внутреннему словарю
                        for rec, title in receipt_collection[key].items():
                            # проверяю условие на содержание букв (в ФИО же нет цифр) вместе с проверкой содержания в соответствующем ключе
                            if (name_or_rec.isdigit() and int(name_or_rec) == key) or (
                                    name_or_rec.isalpha() and name_or_rec in receipt_collection[key]['ФИО владельца техники']):
                                # вывожу словарь
                                print(rec, title, sep=': ')

                    # это для завершения цикла
                    break
                else:
                    print('Неверный ввод!')

                oneMoreTime = input('\nХотите продолжить работу? Введите "Да" или "Нет": ').lower()
                if oneMoreTime != 'да':
                    isTechnicsExists = False

            elif int(num_prog) == 4:

                print('До свидания!')
                isTechnicsExists = False

            else:

                print('Неверный ввод! Попробуйте ещё раз.')


rec1 = Receipt()
rec1.run()
