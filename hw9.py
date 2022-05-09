# encapsulation & polymorphism
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self):

        email = str(input('Введите новый email: '))

        for symb in email:

            if email.count('@') > 1 and '.' not in email:

                return print('Ошибочная почта')

            else:

                self.__email = email
        print('Новый email сохранён')



new_pers = UserMail('classicpers', 'classicpers@gmail.com')
new_pers.set_email()

