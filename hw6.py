import re
def password():
    while True:
        password = input('Введите пароль  : ')
        repassword = input('Повторите пароль: ')
        symbol_regex = r'[%@#$&*!~]'
        is_different = password != repassword
        easy_pass = (password.find('123') != -1) or (password.find('password') != -1)
        counter_digit = 0
        counter_str_upper = 0
        counter_str_lower = 0
        counter_special_symbols = 0
        for i in password:
            if i.isdigit():
                counter_digit += 1
            elif i.isupper():
                counter_str_upper += 1
            elif i.islower():
                counter_str_lower += 1
            elif re.search(i, symbol_regex):
                counter_special_symbols += 1
        counter_str = counter_str_lower + counter_str_upper
        if easy_pass:
            print('Простой!')
        elif is_different:
            print('Различаются!')
        elif len(password) < 12 \
                or counter_digit < 3 \
                or counter_str < 3 \
                or counter_str_upper < 1 \
                or counter_special_symbols < 1:
            print('Пароль должен содержать как минимум 3 цифры, 3 буквы, 1 символ (%@#$&*!~), 1 заглавную букву, состоять как минимум из 12 символов')
        else:
            print('OK')
            break


equate = lambda a, b: print((a + 4 * b) * (a - 3 * b) + a)

greeting = lambda name: print('Hello, ', name)

def scrubble():
    word = input('Type your word: ')
    word = word.upper()
    sum_word = 0
    letters = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
        2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
        3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
        4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
        5: ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
        8: ['J', 'X', 'Ш', 'Э', 'Ю'],
        10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']}
    for letter in word:
        for k, v in letters.items():
            for val in v:
                if letter == val:
                    sum_word += k
    return print(sum_word)

def mail():
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
    for domen, names in sorted(emails.items()):
        for name in names:
            print(name + '@' + domen)
    # print(*sorted({value + '@' + key for key, v in emails.items() for value in v}), sep='\n')

def pets():
    cats = [('Мартин', 5, 'Алексей Егоров'),
            ('Фродо', 3, 'Анна Самохина'),
            ('Вася', 4, 'Андрей Белов'),
            ('Муся', 7, 'Игорь Бероев'),
            ('Изольда', 2, 'Игорь Бероев'),
            ('Снейп', 1, 'Марина Апраксина'),
            ('Лютик', 4, 'Виталий Соломин'),
            ('Снежок', 3, 'Марина Апраксина'),
            ('Марта', 5, 'Сергей Колесников'),
            ('Буся', 12, 'Алена Федорова'),
            ('Джонни', 10, 'Игорь Андропов'),
            ('Мурзик', 1, 'Даниил Невзоров'),
            ('Барсик', 2, 'Виталий Соломин'),
            ('Рыжик', 7, 'Владимир Медведев'),
            ('Матильда', 8, 'Андрей Белов'),
            ('Гарфилд', 3, 'Александр Березуев')]
    cat_info = []
    name = input('Введите имя владельца: ')
    for cat in cats:
        owner = cat[2]
        if name in owner:
            cat_info.append(str(cat[0]) + '(' + str(cat[1]) + ')')
    print('ВЛАДЕЛЕЦ: ' + name + ' ПИТОМЦЫ(ВОЗРАСТ): ' + '; '.join(cat_info))

def friendly():
    for i in range(200, 301):
        firstsum = 0
        secondsum = 0
        for k in range(1, i):
            if i % k == 0:
                firstsum += k
        for j in range(1, firstsum):
            if firstsum % j == 0:
                secondsum += j
        if i == secondsum and i != firstsum and i == min(i, firstsum):
            print(secondsum, firstsum)

lst = [1, 2, "str", [1, 2, 3, [1, 2, 3]]]
def rec(our_list):
    print(', '.join(map(str, our_list)))
    for item in our_list:
        if type(item) == list:
            rec(item)
rec(lst)