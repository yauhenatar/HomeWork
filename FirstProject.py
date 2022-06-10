import collections
from datetime import datetime, timedelta
import random




class Phone:

    def get_info(self):
        self.brand = input('Марка: ')
        self.os = input('Операционная система: ')
        self.brake_info = input('Описание поломки: ')

class Notebook:

    def get_info(self):
        self.brand = input('Марка: ')
        self.os = input('Операционная система: ')
        self.issue_year = input('Год выпуска: ')
        self.brake_info = input('Описание поломки: ')


class TV:

    def get_info(self):
        self.brand = input('Марка: ')
        self.diagonal = input('Диагональ экрана: ')
        self.brake_info = input('Описание поломки: ')


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
        receipt_collection = {}
        rec_num = 1
        technics_list = ['телефон', 'ноутбук', 'телевизор']
        isTechnicsExists = True

        while isTechnicsExists:

            self.full_name = input('Введите ваши ФИО: ')
            self.prod_type = input('Введите тип техники, который сдаёте в ремонт (телефон, ноутбук, телевизор): ').lower()
            if self.prod_type not in technics_list:
                print('Неправильно введена техника! Попробуйте ещё раз')
            else:
                if self.prod_type == 'телефон':
                    prod = Phone()
                elif self.prod_type == 'ноутбук':
                    prod = Notebook()
                elif self.prod_type == 'телевизор':
                    prod = TV()

                prod.get_info()

                if self.prod_type == 'телефон':
                    total_receipt = '\nНомер квитанции: ' + str(1 if len(receipt_collection) == 0 else rec_num + 1) \
                                + '\nФИО владельца техники: ' + str(self.full_name) \
                                + '\nТип изделия: ' + str(self.prod_type) \
                                + '\nБренд: ' + str(prod.brand) \
                                + '\nОперационная система: ' + str(prod.os) \
                                + '\nОписание поломки: ' + str(prod.brake_info) \
                                + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                elif self.prod_type == 'ноутбук':
                    total_receipt = '\nНомер квитанции: ' + str(1 if len(receipt_collection) == 0 else rec_num + 1) \
                                + '\nФИО владельца техники: ' + str(self.full_name) \
                                + '\nТип изделия: ' + str(self.prod_type) \
                                + '\nБренд: ' + str(prod.brand) \
                                + '\nОперационная система: ' + str(prod.os) \
                                + '\nГод выпуска: ' + str(prod.issue_year) \
                                + '\nОписание поломки: ' + str(prod.brake_info) \
                                + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                elif self.prod_type == 'телевизор':
                    total_receipt = '\nНомер квитанции: ' + str(1 if len(receipt_collection) == 0 else rec_num + 1) \
                                + '\nФИО владельца техники: ' + str(self.full_name) \
                                + '\nТип изделия: ' + str(self.prod_type) \
                                + '\nБренд: ' + str(prod.brand) \
                                + '\nДиагональ экрана: ' + str(prod.diagonal) \
                                + '\nОписание поломки: ' + str(prod.brake_info) \
                                + '\nДата приемки: ' + str(self._info_core.accept_date.strftime('%d.%m.%Y')) \
                                + '\nДата выполнения ремонта: ' + str(self._info_core.repair_date.strftime('%d.%m.%Y'))

                receipt_collection.update({1 if len(receipt_collection) == 0 else rec_num + 1: total_receipt})

                print(total_receipt)

                print(receipt_collection)

                oneMoreTechnics = input('\nХотите сдать еще одну технику в ремонт? Введите "Да" или "Нет": ').lower()
                if oneMoreTechnics != 'да':
                    isTechnicsExists = False


rec1 = Receipt()
rec1.run()