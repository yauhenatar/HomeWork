from app.common.CommonOperations import CommonOperations
from app.common.Constants import Constants
from app.workshop.Collections import Collections

"""класс для добавления в квитанцию всей информации о технике"""
class Repair:

    @staticmethod
    def add_technics(class_obj):

        class_obj.receipt_id = 1
        if len(Collections.receipts) > 0:
            class_obj.receipt_id = len(Collections.receipts) + 1

        class_obj.full_name = input('Введите ваши ФИО: ')
        class_obj.prod_type = input(
            'Введите тип техники, который сдаёте в ремонт (телефон, ноутбук, телевизор): ').lower()

        if class_obj.prod_type not in (Constants.PHONE, Constants.NOTEBOOK, Constants.TV):
            print('Неправильно введена техника! Попробуйте ещё раз.')
        else:
            prod = CommonOperations.get_tech_by_type(class_obj.prod_type)
            prod.get_info()

            results = {'Номер квитанции': (str(class_obj.receipt_id)),
                             'ФИО владельца техники': (str(class_obj.full_name)),
                             'Тип изделия': (str(class_obj.prod_type)),
                             'Бренд': (str(prod.brand))}
            if class_obj.prod_type == Constants.PHONE:
                results.update({'Операционная система': (str(prod.os))})

            elif class_obj.prod_type == Constants.NOTEBOOK:
                results.update({'Операционная система': (str(prod.os)),
                                      'Год выпуска': (str(prod.issue_year))})

            elif class_obj.prod_type == Constants.TV:
                results.update({'Диагональ экрана': (str(prod.diagonal))})
            results.update({'Описание поломки': (str(prod.brake_info)),
                             'Дата приемки': (
                                 str(class_obj.info_core.accept_date.strftime('%d.%m.%Y'))),
                             'Дата выполнения ремонта': (
                                 str(class_obj.info_core.repair_date.strftime('%d.%m.%Y'))),
                             'Статус ремонта': (str(class_obj.info_core.status))})

            Collections.receipts.update({class_obj.receipt_id: results})

            for rec, title in results.items():
                print(rec, title, sep=': ')
