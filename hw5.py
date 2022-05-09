"""
func = lambda movie, cinema, time: print('Билет на ' + movie + ' в кинотеатре ' + cinema + ' на ' + time + ' забронирован')
func('"Остров проклятых"', '"Победа"', '13:00')
"""

def smallest(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print(num1)
    if num2 < num1 and num2 < num3:
        print(num2)
    if num3 < num1 and num3 < num2:
        print(num3)


def smallest2(num1, num2, num3):
    nums = sorted([num1, num2, num3])
    print(nums[0])

"""
n = int(input('Веведите количество земных лет '))
const = 365 / 687
func2 = lambda x, y: print(x * y)
func2(x = n, y = const)
"""

import random
def get_random_array(n = 10):
    rng = int(input('Введите длину массива: '))
    numbers = list(range(n))
    random.shuffle(numbers)
    if n > 0:
        print(numbers[:n])
    else:
        print('Введено неверное значение. Допустимое значение: 1 и больше')
    if n > 0:
        print(random.shuffle(list(range(n))))
    else:
        print('Введено неверное значение. Допустимое значение: 1 и больше')

def sum_of_digits(num):
    summa = 0
    for i in str(num):
        summa = summa + int(i)
    print(summa)

def sum_of_digits2(num):
    summa = 0
    while True:
        if num > 10:
            summa = summa + (num % 10)
            num = num // 10
        elif num < 10:
            summa = summa + num
            print(summa)
            break

def factorial(n):
    factorial = 1
    for i in range(2, n+1):
        factorial = factorial * i
    print('!', n, '=', factorial)

def average(*args):
    summa = 0
    for dig in args:
        summa += dig
    print(round(summa/len(args), 2))
