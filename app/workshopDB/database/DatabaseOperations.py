import sqlite3
from sqlite3 import Error

from app.common.Constants import Constants
from app.workshopDB.database.Database import PATH

"""класс операций в бд:
    проверка входа админа
    показать всех админов
    показать пследнюю добавленую квитанцию для вывода после добавления данных о технике
    поиск квитанции по номеру id
    вывод квитанции по id или ФИО
    удалить админа
    добавить админа
    создание новой квитанции
    обновить статус ремонта
    обновить дату выполнения ремонта
    """
class DatabaseOperations:

    @staticmethod
    def select_admin(login, password, connection=None, results=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admins WHERE login = ? AND password = ?", (login, password))
            results = cursor.fetchall()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

        return results

    @staticmethod
    def select_all_admins(connection=None, results=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admins")
            results = cursor.fetchall()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

        return results

    @staticmethod
    def select_last_receipt(connection=None, results=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM receipt WHERE id = (SELECT MAX(id) FROM receipt)")
            results = cursor.fetchall()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

        return results

    @staticmethod
    def select_receipt_by_id(receipt_id, connection=None, results=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM receipt WHERE id = ?", [receipt_id])
            results = cursor.fetchall()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

        return results

    @staticmethod
    def select_receipt_by_id_or_fio(name_or_rec, connection=None, results=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM receipt WHERE id = ? OR full_name = ?", (name_or_rec, name_or_rec))
            results = cursor.fetchall()
            cursor.close()

        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

        return results

    @staticmethod
    def delete_admin(login, connection=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            connection.execute("DELETE FROM admins WHERE login = ?", [login])
            connection.commit()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def insert_admin(full_name, login, password, connection=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO admins (full_name, login, password) "
                           "VALUES(?, ?, ?)", (full_name, login, password))
            connection.commit()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def insert_receipt(class_obj, prod, connection=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()

            if class_obj.prod_type == Constants.PHONE:
                cursor.execute(
                    "INSERT INTO receipt (full_name, prod_type, brand, os, brake_info, accept_date, repair_date, status) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (
                        class_obj.full_name, class_obj.prod_type, prod.brand, prod.os, prod.brake_info,
                        class_obj.info_core.accept_date.strftime('%d.%m.%Y'),
                        class_obj.info_core.repair_date.strftime('%d.%m.%Y'), class_obj.info_core.status))

            elif class_obj.prod_type == Constants.NOTEBOOK:
                cursor.execute(
                    "INSERT INTO receipt (full_name, prod_type, brand, os, issue_year, brake_info, accept_date, repair_date, status) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        class_obj.full_name, class_obj.prod_type, prod.brand, prod.os, prod.issue_year,
                        prod.brake_info,
                        class_obj.info_core.accept_date.strftime('%d.%m.%Y'),
                        class_obj.info_core.repair_date.strftime('%d.%m.%Y'), class_obj.info_core.status))

            elif class_obj.prod_type == Constants.TV:
                cursor.execute(
                    "INSERT INTO receipt (full_name, prod_type, brand, diagonal, brake_info, accept_date, repair_date, status) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (
                        class_obj.full_name, class_obj.prod_type, prod.brand, prod.diagonal, prod.brake_info,
                        class_obj.info_core.accept_date.strftime('%d.%m.%Y'),
                        class_obj.info_core.repair_date.strftime('%d.%m.%Y'), class_obj.info_core.status))

            connection.commit()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def update_status(new_status, receipt_id, connection=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("UPDATE receipt SET status = ? WHERE id = ?", (new_status, receipt_id))
            connection.commit()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def update_repair_date(new_repair_date, receipt_id, connection=None):
        try:
            connection = sqlite3.connect(PATH)
            cursor = connection.cursor()
            cursor.execute("UPDATE receipt SET repair_date = ? WHERE id = ?", (new_repair_date, receipt_id))
            connection.commit()
            cursor.close()
        except Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if connection:
                connection.close()
