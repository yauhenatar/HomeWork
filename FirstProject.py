import collections
from datetime import datetime, timedelta
import random

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


    def get_repair_date(self):
        return self.accept_date + timedelta(days=random.randint(1, 5))


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

            print('Если хотите сдать технику в ремонт, введите 1'
                  '\nЕсли хотите посмотреть информацию, введите 2'
                  '\nЕсли хотите выйти, введите 3')
            num_prog = input('Ваш выбор: ')

            if int(num_prog) == 1:

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
                        total_receipt = '\nНомер квитанции: ' + str(self.rec_num) \
                                        + '\nФИО владельца техники: ' + str(self.full_name) \
                                        + '\nТип изделия: ' + str(self.prod_type) \
                                        + '\nБренд: ' + str(prod.brand) \
                                        + '\nОперационная система: ' + str(prod.os) \
                                        + '\nОписание поломки: ' + str(prod.brake_info) \
                                        + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                        + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                    elif self.prod_type == 'ноутбук':
                        total_receipt = '\nНомер квитанции: ' + str(self.rec_num) \
                                        + '\nФИО владельца техники: ' + str(self.full_name) \
                                        + '\nТип изделия: ' + str(self.prod_type) \
                                        + '\nБренд: ' + str(prod.brand) \
                                        + '\nОперационная система: ' + str(prod.os) \
                                        + '\nГод выпуска: ' + str(prod.issue_year) \
                                        + '\nОписание поломки: ' + str(prod.brake_info) \
                                        + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                        + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                    elif self.prod_type == 'телевизор':
                        total_receipt = '\nНомер квитанции: ' + str(self.rec_num) \
                                        + '\nФИО владельца техники: ' + str(self.full_name) \
                                        + '\nТип изделия: ' + str(self.prod_type) \
                                        + '\nБренд: ' + str(prod.brand) \
                                        + '\nДиагональ экрана: ' + str(prod.diagonal) \
                                        + '\nОписание поломки: ' + str(prod.brake_info) \
                                        + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                        + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                    receipt_collection.update({self.rec_num: total_receipt})

                    print(total_receipt)
                    print(receipt_collection)

                    oneMoreTime = input('\nХотите продолжить работу? Введите "Да" или "Нет": ').lower()
                    if oneMoreTime != 'да':
                        isTechnicsExists = False

            elif int(num_prog) == 2:

                infoFlag = True

                while infoFlag:
                    name_or_rec = str(input('Введите ФИО или номер квитанции: '))

                    for rec, rec_title in receipt_collection.items():
                        if (name_or_rec.isdigit() and int(name_or_rec) == rec) or (
                                name_or_rec.isalpha() and name_or_rec in rec_title):
                            print(receipt_collection[rec])
                            break
                    else:
                        print('Неправильно введено значение!')

                    answer = input('\nХотите посмотреть информацию по другой технике? Введите "Да" или "Нет": ').lower()
                    if answer != 'да':
                        infoFlag = False

                oneMoreTime = input('\nХотите продолжить работу? Введите "Да" или "Нет": ').lower()
                if oneMoreTime != 'да':
                    isTechnicsExists = False

            elif int(num_prog) == 3:

                print('До свидания!')
                isTechnicsExists = False

            else:

                print('Введён неверный номер! Попробуйте ещё раз.')


rec1 = Receipt()
rec1.run()