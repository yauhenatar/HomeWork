from app.common.Constants import Constants
from app.technics.Technics import Phone, Notebook, TV


class CommonOperations:
    """ Класс, который содержит операции, которые могут использоваться по всему проекту"""

    @staticmethod
    def get_tech_by_type(prod_type):
        """ Возвращает модель техники в зависимости от типа устройства, которое клиент сдает в ремонт """

        if prod_type == Constants.PHONE:
            return Phone()
        elif prod_type == Constants.NOTEBOOK:
            return Notebook()
        elif prod_type == Constants.TV:
            return TV()

    @staticmethod
    def continue_or_exit(is_exit=False):
        """ Финальная проверка перед выходом из проекта """

        print('\n[ВЫ ТОЧНО ХОТИТЕ ВЫЙТИ?]\nД - ВЫХОД\tН - ОСТАТЬСЯ')
        choise = input('\nВаш выбор: ').upper()

        if choise == 'Д':
            print('\nДо свидания!')
            is_exit = True

        return is_exit

    @staticmethod
    def show_receipt(results):
        """ Вывод на консоль квитанции в режиме с БД"""

        for row in results:
            print('Номер квитанции:', row[0],
                  '\nФИО владельца техники:', row[1],
                  '\nТип изделия:', row[2])

            if row[2] == Constants.PHONE:
                print('Бренд:', row[3],
                      '\nОперационная система:', row[4])

            elif row[2] == Constants.NOTEBOOK:
                print('Бренд:', row[3],
                      '\nОперационная система:', row[4],
                      '\nГод выпуска:', row[6])

            elif row[2] == Constants.TV:
                print('Бренд:', row[3],
                      '\nДиагональ экрана:', row[5])

            print('Описание поломки:', row[7],
                  '\nДата приемки:', row[8],
                  '\nДата выполнения ремонта:', row[9],
                  '\nСтатус ремонта:', row[10])
