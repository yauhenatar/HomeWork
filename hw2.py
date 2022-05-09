#zoloto
"""
print("Введите фразу")
a = input()
if "золото" in a:
    print("Да")
else:
    print("Нет")
"""
#ekzamen
"""
print("Какая у тебя оценка?")
a = int(input())
if a > 0 and a < 40:
    print("Не очень")
elif a > 41 and a < 60:
    print("Неплохо")
elif a > 61 and a < 80:
    print("Хорошо")
elif a > 81 and a < 90:
    print("Отлично")
else:
    print("Невероятно")
    """
#zapros
"""
print("Сколько тебе лет?")
a = int(input())
if a > 20:
    print("Вы уверены?")
    b = input()
    if "Да" in b or "да" in b or "конечно" in b:
        print("Доступ разрешён!")
"""
#calc
"""
a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    if b != 0:
        print(a/b)
    else:
        print("error")
else:
    print("error")
"""
#stroki
"""
s = 'Строки на Python'
s1 = s*7
s2 = str(s+s1)
print(s, s1, s2, sep=',')
"""
#f-s
"""
string = str(input())
first = string[0]
last = string[-1]
print(first, last, sep=' ')
"""
#zamena
"""
string = input("Введите переменную: ")
new_string = string.split()
need_one = new_string[0]
new_string[0] = need_one[-1] + need_one[1:-1] + need_one[0]
print(string, new_string[0])
"""
#reverse
"""
string = input("Введите переменную: ")
new_string = string[::-1]
print(string, new_string)
"""
#tri slova
"""
s = input("Введите строку: ")
a = s.split()
b = a[0].count('a')
print(b)
if 'a' in a[1]:
    c = a[1].replace('a','A')
    print(c)
else:
    print('error')
"""
#password ne reshen
"""
pw = input('Введите пароль: ')

if pw.isdigit() and pw.isalpha():
    print('True')
else:
    print('False')
"""
#ne moe rewenie password
"""
from string import digits, ascii_letters

password = input()

let = False

dig = False

No_space = True

for i in password:

 if i == " ":

   No_space = False

 elif (dig != True) and (i in digits):

   dig = True

 elif (let != True) and (i in ascii_letters):

   let = True

if let and dig and No_space:

 print('True')

else: 
 print("False")
"""
#slovari
"""
solar_system = dict(Jupiter='1321', Mars='0.15', Saturn='764')
solar_system['Mercury'] = 0.05
solar_system['Venus'] = 0.86
solar_system['Neptune'] = 57.7
solar_system['Pluto'] = 0.059
solar_system['Earth'] = 1
print(solar_system)
solar_system.pop('Pluto')
print(solar_system)
"""
#pythonist
"""
s = 'pythonist'
d = {i:s.count(i) for i in s}
print(d)
"""
#slovar' auto
"""
auto = {}
auto['BMW'] = 'Serie_M', 'Serie_X', 'Serie_E'
auto['Tesla'] = 'Model_S', 'Model_X', 'Model_Y'
for key, value in auto.items():
    print(key, value[0::2])
"""