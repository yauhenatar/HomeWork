class Technics:

    def __init__(self):
        self.brand = input('Марка: ')
        self.brake_info = input('Описание поломки: ')


class Phone(Technics):

    def get_info(self):
        self.os = input('Операционная система: ')


class Notebook(Technics):

    def get_info(self):
        self.os = input('Операционная система: ')
        self.issue_year = input('Год выпуска: ')


class TV(Technics):

    def get_info(self):
        self.diagonal = input('Диагональ экрана: ')
