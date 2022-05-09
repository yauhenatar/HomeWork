#numbers

def task_n1(a, b):
    return print('Сумма равна ', a + b,
                 '\nРазность равна ', a - b,
                 '\nПроизведение равно ', a * b,
                 '\nРезультат деления ', round(a / b, 2),
                 '\nРезультат целочисленного деления ', a // b,
                 '\nОстаток от деления равен ', a % b)

def task_n2(x, y):
    return print((abs(x) - abs(y)) / (1 + abs(x * y)))


def task_n3(edge):
    return print('Объём куба равен ', edge ** 3,
                 'Площадь боковой поверхности куба равна ', edge ** 2)


def task_n4(num1, num2):
    return print('Среднее арифметическое чисел ', (num1 + num2) / 2,
                 'Среднее геометрическое чисел ', (num1 * num2) ** 0.5)


def task_n5(leg1, leg2):
    return print('Гипотенуза равна ', (leg1 ** 2 + leg2 ** 2) ** 0.5,
                 'Площадь равна ', 0.5 * leg1 * leg2)

# strings

def task_s1(string):
    return print(string[2])

def task_s2(string):
    return print(string[-2])

def task_s3(string):
    return print(string[:6])

def task_s4(string):
    return print(string[:-2])

def task_s5(string):
    return print(string[::2])

# dictionaries

def task_d1(list1, list2):
    uniq_list1 = set(list1)
    uniq_list2 = set(list2)
    new_dict = dict(zip(uniq_list1, uniq_list2))
    return print(new_dict)


dict1 = { 'a': [1, 3, 2], 'b': [6], 'c': [0, 0] }
def task_d2(our_dict):
    for key, value in our_dict.keys:
        if key == 'key':
            print(our_dict['key'])
        else:
            print(our_dict.key)
task_d2(dict1)