from app.common.CommonOperations import CommonOperations
from app.workshopDB.database.DatabaseOperations import DatabaseOperations

"""реализация всего админ-меню"""

class AdminPanelDBOperations:

    @staticmethod
    def check_login(is_admin=False):

        while not is_admin:
            print('\nАВТОРИЗАЦИЯ')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')

            results = DatabaseOperations.select_admin(login, password)
            if len(results) == 1:
                for row in results:
                    print(f'Добро пожаловать, {row[1]}')
                    is_admin = True
            else:
                print('Неправильное имя пользователя или пароль! Попробуйте ещё раз')
                print("0 - Назад\t9 - Повторить")
                if int(input()) == 0:
                    break

        return is_admin

    @staticmethod
    def get_all_admins():
        results = DatabaseOperations.select_all_admins()
        AdminPanelDBOperations.show_all_admins(results)

    @staticmethod
    def delete_admin():
        login = input('Введите логин удаляемого администратора: ')
        DatabaseOperations.delete_admin(login)
        print('Удаление прошло успешно')

    @staticmethod
    def add_new_admin():
        full_name = input('Введите ФИО добавляемого администратора: ')
        login = input('Введите логин добавляемого администратора: ')
        password = input('Введите пароль добавляемого администратора: ')

        DatabaseOperations.insert_admin(full_name, login, password)
        print("Админ успешно добавлен")

    @staticmethod
    def change_receipt_status(receipt_id):
        new_status = input('\nВведите новый статус ремонта техники: ')
        DatabaseOperations.update_status(new_status, receipt_id)

    @staticmethod
    def change_receipt_repair_date(receipt_id):
        new_repair_date = input('\nВведите новую дату ремонта техники: ')
        DatabaseOperations.update_repair_date(new_repair_date, receipt_id)

    @staticmethod
    def get_receipt_info(receipt_id):
        results = DatabaseOperations.select_receipt_by_id(receipt_id)
        CommonOperations.show_receipt(results)

    @staticmethod
    def show_all_admins(results):
        for row in results:
            print('\n')
            print(f'ФИО администратора: {row[1]}',
                  f'Логин: {row[2]}',
                  f'Пароль: {row[3]}', sep='\n')
