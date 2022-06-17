from app.common.Constants import Constants
from app.workshop.operations.AdminPanelOperations import AdminPanelOperations
"""адмнин-меню, всё тут прописано для выбора того, что в админ-панель операциях прописано
прописано методом match/case, что реализовано в python 3.10"""

class AdminPanel:

    @staticmethod
    def admin_panel():
        is_admin = AdminPanelOperations.check_login()

        while is_admin:
            print(Constants.MENU_ADMIN_PANEL)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: AdminPanelOperations.get_all_admins()
                    case 2: AdminPanelOperations.delete_admin()
                    case 3: AdminPanelOperations.add_admin()
                    case 4: AdminPanel.receipt_menu()
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
                    case 1: AdminPanelOperations.change_receipt_status(receipt_id)
                    case 2: AdminPanelOperations.change_receipt_repair_date(receipt_id)
                    case 3: AdminPanelOperations.get_receipt_info(receipt_id)
                    case 0: break
                    case _: print('Неверный ввод! Попробуйте ещё раз')
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')