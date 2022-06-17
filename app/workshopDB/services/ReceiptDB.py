from app.common.CommonOperations import CommonOperations
from app.workshopDB.database.DatabaseOperations import DatabaseOperations
"""класс для получения информации в квитанции по id или ФИО"""

class ReceiptDB:

    @staticmethod
    def get_receipt_info():
        name_or_rec = str(input('Введите ФИО или номер квитанции: '))
        results = DatabaseOperations.select_receipt_by_id_or_fio(name_or_rec)
        CommonOperations.show_receipt(results)
