from app.workshop.Collections import Collections
"""класс операций в админ-панели:
    проверка логина
    получение всех админов
    удалить админа
    добавить админа
    работа с квитанциями:
        изменить статус ремонта
        изменить дату ремонта
        посмотреть информацию о квитанции
    """

class AdminPanelOperations:

    @staticmethod
    def check_login(is_admin=False):

        while not is_admin:
            print('\nАВТОРИЗАЦИЯ')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            for key, value in Collections.admins.items():
                if login == value[0] and password == value[1]:
                    print(f'Добро пожаловать, {value[2]}')
                    is_admin = True
                    return is_admin
            else:
                print('Неправильное имя пользователя или пароль! Попробуйте ещё раз')
                print("0 - Назад\t9 - Повторить")
                choise = int(input())
                if choise == 0:
                    return is_admin


    @staticmethod
    def get_all_admins():
        print('Список администраторов (в формате логин, пароль, ФИО админа): ')
        for key, value in Collections.admins.items():
            print(Collections.admins[key])


    @staticmethod
    def delete_admin():
        admin_info = str(input('Введите логин или ФИО админа, которого нужно удалить: '))
        new_admins = Collections.admins.copy()
        for key, value in new_admins.items():
            if admin_info in value:
                del Collections.admins[key]
                print('Операция выполнена')

    @staticmethod
    def add_admin():
        login = input('Введите логин администратора: ')
        password = input('Введите пароль администратора: ')
        full_name = input('Введите ФИО администратора: ')

        new_admin = [login, password, full_name]
        new_admin_id = len(Collections.admins.keys()) + 1
        Collections.admins[new_admin_id] = new_admin
        print('Операция выполнена')

    @staticmethod
    def change_receipt_status(receipt_id):
        new_status = input('\nВведите новый статус ремонта техники: ')
        for key in Collections.receipts.keys():
            if receipt_id.isdigit() and int(receipt_id) == key:
                Collections.receipts[key]['Статус ремонта'] = new_status

    @staticmethod
    def change_receipt_repair_date(receipt_id):
        new_rep_date = input('\nВведите новую дату ремонта техники: ')
        for key in Collections.receipts.keys():
            if receipt_id.isdigit() and int(receipt_id) == key:
                Collections.receipts[key]['Дата выполнения ремонта'] = new_rep_date


    @staticmethod
    def get_receipt_info(receipt_id):

        while True:

            for key in Collections.receipts.keys():
                for rec, title in Collections.receipts[key].items():
                    if receipt_id.isdigit() and int(receipt_id) == key:
                        print(rec, title, sep=': ')
            break
