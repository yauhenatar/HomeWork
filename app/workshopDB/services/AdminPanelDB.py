from app.common.Constants import Constants
from app.workshopDB.operations.AdminPanelDBOperations import AdminPanelDBOperations

"""класс прописанной менюшки админ-панели"""
class AdminPanelDB:

    @staticmethod
    def admin_panel():
        is_admin = AdminPanelDBOperations.check_login()

        while is_admin:
            print(Constants.MENU_ADMIN_PANEL)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: AdminPanelDBOperations.get_all_admins()
                    case 2: AdminPanelDBOperations.delete_admin()
                    case 3: AdminPanelDBOperations.add_new_admin()
                    case 4: AdminPanelDB.receipt_menu()
                    case 0: break
                    case _: print('Неверный ввод! Попробуйте ещё раз')
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    @staticmethod
    def receipt_menu():
        while True:
            receipt_id = str(input('\nВведите номер квитанции, с которой желаете работать: '))

            print(Constants.MENU_ADMIN_PANEL_CHANGE_RECEIPT)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: AdminPanelDBOperations.change_receipt_status(receipt_id)
                    case 2: AdminPanelDBOperations.change_receipt_repair_date(receipt_id)
                    case 3: AdminPanelDBOperations.get_receipt_info(receipt_id)
                    case 0: break
                    case _: print('Неверный ввод! Попробуйте ещё раз')
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')