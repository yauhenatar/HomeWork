class Matter:

    def __init__(self, uni_num, uni_law):
        self.uni_num = uni_num
        self.uni_law = uni_law

    @staticmethod
    def uni_info(uni_num = 0, uni_law = 'standart'):
        print(f"я вселенная номер «{uni_num}», я имею закон «{uni_law}»")

    @classmethod
    def change_uni_num(cls, new_uni_num):
        cls.uni_num = new_uni_num

    @classmethod
    def change_uni_law(cls, new_uni_law):
        cls.uni_law = new_uni_law

class Human(Matter):

    race = 'русский'
    skin_color = 'белый'
    language = 'русском'

    counter = 0

    def __init__(self, name, age, country='Россия'):
        self.name = name
        self.age = age
        self.__country = country
        self.adult = False if age < 18 else True
        Human.counter += 1

    @classmethod
    def new_one(cls, name, year):
        from datetime import datetime as dt
        return cls(name, (dt.now().year-year))

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def can_drive(self):
        return print(f"{self.name} может водить авто при наличии документа, позволяющего управлять ТС"\
        if self.adult == True else f"{self.name} не может водить авто")

    def hum_info(self):
        return print(f"{self.name} живёт в {self.get_country()}, его раса  - {Human.race}")

    def hum_language(self):
        return print(f"{self.name} как и другие русские люди говорит на {Human.language} языке")

    @staticmethod
    def race_skin(race, skin_color):
        return print(f"У людей расы {race} обычно {skin_color} цвет кожи")

    @staticmethod
    def hum_status(country, age):
        return print(f"В {country} в возрасте {age} лет люди обычно учатся" if age <= 25 else \
                     f"В {country} в возрасте {age} лет люди уже работают")

class Car(Matter):

    body = 'кроссовер'              #кузов
    engine_type = 'бензиновый'          #тип двигателя
    appointment = 'персонального использования'     #назначение

    counter = 0

    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage                  #пробег
        Car.counter += 1

    @classmethod
    def new_one(cls, brand, model, year, mileage=28300):
        return cls(brand, model, year, mileage=28300+15000 if year < 2020 else 28300)

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def car_info(self):
        return print(f"Эта машина {self.brand} {self.model}, {self.year} года выпуска")

    def mileage_info(self):
        return print(f"У этой машины пробег составляет {self.get_mileage()} километров")

    def body_type(self):
        return print(f"У {self.brand} {self.model} кузов типа {Car.body}")

    @staticmethod
    def engine_info(brand, model, engine_type):
        return print(f"Двигатель автомобиля {brand} {model} {engine_type}")

    @staticmethod
    def appointment_info(brand, model, appointment):
        return print(f"{brand} {model} предназначен для {appointment} на любых участках дорог")

class Hippopotamus(Matter):

    ani_class = 'Млекопитающие'
    order = 'Парнокопытные'
    genus = 'Бегемоты'

    counter = 0

    def __init__(self, height, length, age, maxspeed=0):
        self.height = height                   #высота
        self.length = length                     #длина
        self.__age = age
        self.__maxspeed = 48 if age >= 15 else 27
        Hippopotamus.counter += 1

    @classmethod
    def new_one(cls, height, length, age, maxspeed=0):
        return cls(height, length, age, maxspeed)

    def get_maxspeed(self):
        return self.__maxspeed

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def hip_info(self):
        return print(f"Нашему бегемоту {self.get_age} лет. Он достиг {self.length} метров длины и {self.height} метров высоты")

    def maxspeed_info(self):
        return print(f"Взрослые особи бегемотов достигают максимальной скорости бега в {self.get_maxspeed()} км/ч")

    def interest_fact(self):
        return print(f"Бегемот - единственный современный вид рода {Hippopotamus.genus}")

    @staticmethod
    def basic_info(ani_class, order):
        return print(f"Бегемоты относятся к классу {ani_class}, отряду {order}")

    @staticmethod
    def hip_genus(genus):
        return print(f"Семейство бегемотов - {genus}")

class Computer(Matter):

    appointment = 'персональный компьютер' #назначение
    mobility = 'не переносной'             #мобильность
    capabilities = 'общего'               #способности: 1 ф-я, несколько ф-й, общего назначения

    counter = 0

    def __init__(self, core_num, RAM, start_time, ssd=False):
        self.core_num = core_num                            #кол-во ядер
        self.RAM = RAM                                      #объём оперативной памяти в ГБ
        self.__start_time = start_time                      #время в минутах от нажатия power до готовности работать
        self.ssd = False if start_time > 1.5 else True      #есть ли ссд True/False
        Computer.counter += 1

    @classmethod
    def new_one(cls, core_num,  RAM, start_time, ssd=False):
        return cls(core_num, RAM, start_time, ssd)

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def core_info(self):
        return print(f"Количество ядер нашего компьютера - {self.core_num}")

    def basic_info(self):
        return print(f"В компьютер установлено {self.RAM} Гб оперативной памяти")

    def presence_ssd(self):
            return print("В компьютере установлен ssd диск" if self.ssd == True else "В компьютере не установлен ssd диск")

    @staticmethod
    def cap_info(capabilities):
        return print(f"Наш компьютер по своим способностям - {capabilities} назначения")

    @staticmethod
    def our_comp(appointment, mobility):
        return print(f"Назначение нашего компьютера - {appointment}, его тип {mobility} ")


# milky_way = Matter(1, 'perfect')
# Matter.uni_info()
# milky_way.uni_info(milky_way.uni_num, milky_way.uni_law)
#
# vasya = Human.new_one("Vasily", 1995)
# print(vasya.age)
# print(vasya.get_country())
# vasya.can_drive()
# vasya.hum_info()
# vasya.hum_language()
# vasya.race_skin(Human.race, Human.skin_color)
# Human.hum_status("Russia", 28)
#
# bmw = Car.new_one('BMW', 'X6', 2013)
# print(bmw.get_mileage())
# bmw.car_info()
# bmw.mileage_info()
# bmw.body_type()
# bmw.engine_info(bmw.brand, bmw.model, Car.engine_type)
# bmw.appointment_info(bmw.brand, bmw.model, Car.appointment)
#
# hip = Hippopotamus.new_one(1.3, 4.3, 18)
# print(hip.maxspeed_info())
# hip.hip_info()
# hip.maxspeed_info()
# hip.interest_fact()
# hip.basic_info(Hippopotamus.ani_class, Hippopotamus.order)
# hip.hip_genus(Hippopotamus.genus)
#
# asus = Computer.new_one(4, 16, 1.8)
# print(asus.get_start_time())
# print('Вам стоит купить ssd диск' if asus.ssd == False else 'Ваш компьютер работает очень быстро')
# asus.core_info()
# asus.basic_info()
# asus.presence_ssd()
# asus.cap_info(Computer.capabilities)
# asus.our_comp(Computer.appointment, Computer.mobility)