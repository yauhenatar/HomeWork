from datetime import datetime, timedelta
import random


class Info:

    def __init__(self):
        self.accept_date = datetime.now().date()
        self.repair_date = self.get_repair_date()
        self.status = 'в ремонте'


    def get_repair_date(self):
        return self.accept_date + timedelta(days=random.randint(1, 5))

    def set_status(self):
        self.status = input('Введите статус ремонта (в ремонте, отремонтировано, отдано заказчику): ')