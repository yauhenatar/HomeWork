def zapros():
    while True:
        i = int(input('введите число: '))
        if i == 0:
            break

def schetchik():
    i = 5
    while i < 50:
        print(i)
        i += 1          #i = i+1

def temperatura():
    i = 1
    week = 7
    temp = float(input('Введите температуру: '))
    while temp < 22.0:
        temp = float(input('Введите температуру: '))
        i += 1
        if temp > 22.0:
            print('Прошло недель ожидания ', int((i-1)//week))

def fibonnacci():
    n = int(input('Задайте натуральное число: '))
    ch1 = 1
    ch2 = 1
    summa = ch1 + ch2
    print(ch1, ch2, summa, sep='\n')
    while True:
        ch1 = ch2
        ch2 = summa
        summa = ch1 + ch2
        if summa < n:
            print(summa)
        if summa > n:
            break

def k5c():
    i = 0
    while i <= 100:
        print(i)
        i += 5

def srzn():
    l = []
    n = 0
    while True:
        i = float(input('Введите число: '))
        n += 1
        l.append(i)
        if i == 0:
            print(round(sum(l)/(n-1), 2))
            break

def skidki():
    a = float(input('Введите цену '))
    price = []
    while True:
        if a < 1500:
            price.append(a)
            a = float(input('Введите цену '))
        elif a >= 1500:
            a = float(a - (a * 0.08))
            price.append(a)
            a = float(input('Введите цену '))
        if a < 0:
            break
    print(sum(price))

def rng():
    for i in range(15):
        print(i)
    for i in range(7, 18):
        print(i)

def nechet():
    for i in range(7, -5, -1):
        if i%2 != 0:
            print(i)

def massiv():
    n = int(input('Введите длину массива '))
    a = [0] * n
    for i in range(len(a)):
        i = str(i + 1)
        print("Введите элемент массива ", end=" ")
        i = int(i)
        i = i - 1
        a[i] = int(input())
    count = 0
    result = 0
    for j in range(len(a)-1):
        if a[j+1] > a[j]:
            count += 1
        elif count >= 1 and a[j] > a[j+1]:
            result += 1
            count = 0
    if a[-1] > a[-2]:
        result += 1
    print(result)

def stroka():
    s = 'Привет, крокодил!'
    a = []
    for i in s:
        с = s.count(i)
        if с > 1:
            pass
        else:
            a.append(i)
    print(''.join(a))

def perebor():
    s = 'b22%2mZUk$hv3^b^3s85Q#'
    a = []
    lt = False
    num = False
    for letter in s:
        if letter.isalpha() and not lt:
            a.append('1')
        elif letter.isdigit() and not num:
            a.append('2')
        else:
            a.append('3')
    print(''.join(a))

