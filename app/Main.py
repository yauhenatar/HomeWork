from app.common.CommonOperations import CommonOperations
from app.technics.Info import Info
from app.workshopDB.services.AdminPanelDB import AdminPanelDB
from app.workshopDB.services.ReceiptDB import ReceiptDB
from app.workshopDB.services.RepairDB import RepairDB
from app.workshop.services.AdminPanel import AdminPanel
from app.workshop.services.Receipt import Receipt
from app.workshop.services.Repair import Repair
from app.common.Constants import Constants

"""стартовое меню, в котором идёт выбор между работой с бд и без бд"""


class Main:
    def __init__(self):
        self.info_core = Info()

    def start_menu(self, is_exit=False):
        while not is_exit:
            print(Constants.MENU_START)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: Main.main_menu(self)
                    case 2: Main.main_menu_db(self)
                    case 0: is_exit = CommonOperations.continue_or_exit()
                    case _: print("Неверный выбор")
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    def main_menu(self):
        while True:
            print(Constants.MENU_MAIN)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: AdminPanel.admin_panel()
                    case 2: Repair.add_technics(self)
                    case 3: Receipt.get_receipt_info()
                    case 0: break
                    case _: print('Неверный ввод! Попробуйте ещё раз.')
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    def main_menu_db(self):
        while True:
            print(Constants.MENU_MAIN)
            try:
                match int(input('\nВаш выбор: ')):
                    case 1: AdminPanelDB.admin_panel()
                    case 2: RepairDB.add_technics(self)
                    case 3: ReceiptDB.get_receipt_info()
                    case 0: break
                    case _: print('Неверный ввод! Попробуйте ещё раз.')
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')


Main().start_menu()