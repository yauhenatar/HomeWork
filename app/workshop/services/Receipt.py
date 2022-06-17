from app.workshop.Collections import Collections

"""класс для получения информации по запрошенной квитанции при работе без бд"""
class Receipt:

    @staticmethod
    def get_receipt_info(flag=False):

        name_or_rec = input('Введите ФИО или номер квитанции: ')

        for key in Collections.receipts.keys():
            for rec, title in Collections.receipts[key].items():
                if (name_or_rec.isdigit() and int(name_or_rec) == key) \
                        or (name_or_rec.isalpha() and (name_or_rec in Collections.receipts[key]['ФИО владельца техники'])):
                    print(rec, title, sep=': ')
                    flag = True

        if not flag:
            print('Неверный ввод!')
