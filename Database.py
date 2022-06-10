import sqlite3
from sqlite3 import Error

PATH = "C:\\Users\yauhenatar\PycharmProjects\HomeWork\database\sqlite.db"


def execute_query(query):

    try:
        connection = sqlite3.connect(PATH)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
    except Error as e:
        print(f"Найдена '{e}' ошибка")


receipt = """
CREATE TABLE IF NOT EXISTS receipt (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name   TEXT,
  prod_type   TEXT,
  brand       TEXT,
  os          TEXT,
  diagonal    INTEGER,
  issue_year  INTEGER,
  brake_info  TEXT,
  accept_date TEXT,
  repair_date TEXT,
  status      TEXT
);
"""

admins = """
CREATE TABLE IF NOT EXISTS admins (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  login     TEXT NOT NULL,
  password  TEXT NOT NULL
);
"""

admin = """
INSERT INTO
  admins (full_name, login, password)
VALUES  ('Admin', 'admin', 'admin'),
  ('Лазюк Валерий Семёнович', 'fenya', 'fenyastar1337'),
  ('Лебедев Артемий Батькович', 'artemiy', 'krutoidizayner4ever');
"""

# execute_query(receipt)
# execute_query(admins)
# execute_query(admin)

