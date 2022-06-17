import sqlite3
from sqlite3 import Error

"""создание бд и нужных таблиц"""

PATH = "C:\\Users\\yauhenatar\\PycharmProjects\\HomeWork\\app\\workshopDB\\database\\sqlite.db"


def execute_query(query):
    try:
        connection = sqlite3.connect(PATH)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
    except Error as e:
        print(f"Найдена '{e}' ошибка")


create_table_receipt = """
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

drop_table_admins = """DROP TABLE admins;"""

create_table_admins = """
CREATE TABLE IF NOT EXISTS admins (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  login     TEXT NOT NULL,
  password  TEXT NOT NULL
);
"""

insert_admin = """
INSERT INTO
  admins (full_name, login, password)
VALUES  ('Лазюк Валерий Семёнович', 'fenya', 'fenyastar1337'),
  ('Васин Ростислав Александрович', 'rostik', 'rostikmillion15'),
  ('Лебедев Артемий Батькович', 'artemiy', 'krutoidizayner4ever'),
  ('adminPanel', 'admin', 'admin');
"""

# execute_query(create_table_receipt)
# execute_query(drop_table_admins)
# execute_query(create_table_admins)
# execute_query(insert_admin)
