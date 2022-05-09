def dvcm(a):
    return a * 2.54

def cmvd(a):
    return a * 0.393700787

def mvkm(a):
    return a * 1.609344

def kmvm(a):
    return a * 0.621371192

def fvkg(a):
    return a * 0.45359237

def kgvf(a):
    return a * 2.20462

def uvg(a):
    return a * 28.3495

def gvu(a):
    return a * 0.0352739619

def galvl(a):
    return a * 3.78541

def lvgal(a):
    return a * 0.264172

def pvl(a):
    return a * 0.473176

def lvp(a):
    return a * 2.11338

def convert():
    while True:
        i = int(input('Введите номер конвертера: '))
        if i in range(13):
            if i == 0:
                break
            else:
                n = float(input('Введите число: '))
                if i == 1:
                    print(float(round(dvcm(n), 2)))
                elif i == 2:
                    print(float(round(cmvd(n), 2)))
                elif i == 3:
                    print(float(round(mvkm(n), 2)))
                elif i == 4:
                    print(float(round(kmvm(n), 2)))
                elif i == 5:
                    print(float(round(fvkg(n), 2)))
                elif i == 6:
                    print(float(round(kgvf(n), 2)))
                elif i == 7:
                    print(float(round(uvg(n), 2)))
                elif i == 8:
                    print(float(round(gvu(n), 2)))
                elif i == 9:
                    print(float(round(galvl(n), 2)))
                elif i == 10:
                    print(float(round(lvgal(n), 2)))
                elif i == 11:
                    print(float(round(pvl(n), 2)))
                elif i == 12:
                    print(float(round(lvp(n), 2)))
        else:
            print('Неверный идентефикатор, повторите попытку')



def delitel():
    m = int(input('Введите число начала диапазона: '))
    n = int(input('Введите число окончания диапазона: '))
    for i in range(m, n):
        for j in range(1, n):
            if i % j == 0 and j != 1 and j != i:
                print('Для i=', i, 'делителем будет', j)
