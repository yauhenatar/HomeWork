from app.common.CommonOperations import CommonOperations
from app.common.Constants import Constants
from app.workshopDB.database.DatabaseOperations import DatabaseOperations
"""класс для получения и добавления информации в квитанцию"""

class RepairDB:

    @staticmethod
    def add_technics(class_obj):
        class_obj.full_name = input('Введите ваши ФИО: ')
        class_obj.prod_type = input(
            'Введите тип техники, который сдаёте в ремонт (телефон, ноутбук, телевизор): ').lower()

        if class_obj.prod_type not in (Constants.PHONE, Constants.NOTEBOOK, Constants.TV):
            print('Неправильно введена техника! Попробуйте ещё раз.')

        else:
            prod = CommonOperations.get_tech_by_type(class_obj.prod_type)
            prod.get_info()

            DatabaseOperations.insert_receipt(class_obj, prod)
            results = DatabaseOperations.select_last_receipt()
            CommonOperations.show_receipt(results)
