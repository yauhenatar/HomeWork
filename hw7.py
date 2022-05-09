#задача 1
class Tea:
    def __init__(self, teatype, leaf, country, adds):
        self.teatype = teatype                          #Чёрный, белый, жёлтый, зелёный, улун, пуэр и т.д.
        self.leaf = leaf                                #Чайное дерево, другое растение
        self.country = country                          #Индия, Китай, Тайвань, и т.д.
        self.adds = adds                                #любые виды добавок: цитрусовые, смородина и т.д.

    def cook_method(self):
        print("Воду для чая следует кипятить до точки помутнения, когда пузырьки в воде начинают поднисаться. "
              "Обдаем заварочный чайник 2-3 раза кипятком. Засыпаем столько ложек заварки, сколько человек будет"
              "пить чай. Заливаем воду в чайник наполовину, через 3 минуты наливаем доверху. Ждём 5 минут. Готово!")

    def properties(self):
        print("Чай поддерживает кислотно-щелочной баланс крови благодаря содержанию таких алкалоидов, как кофеин, "
              "теофиллин, теобромин. В организме чай быстро усваивается, в результате чего образуются вещества в "
              "концентрации, достаточной для своевременной нейтрализации кислотных отходов, попадающих в кровь."
              "\nЧай поддерживает кроветворную функцию организма. В чае, кроме того, содержатся вещества, нейтрализующие "
              "вредные излучения, поэтому чаепитие перед включенным телевизором защищает от облучения и сохраняет зрение."
              "\nЧайный танин убивает многие бактерии, и поэтому предотвращает стоматиты, ангины, энтериты и другие "
              "кишечные инфекции. \nЧай стимулирует центральную нервную систему и увеличивает подвижность суставов."
              "\nЧай подавляет рост злокачественных опухолей, и существенно снижает риск перерождения клеток в раковые.")


class Purse:
    def __init__(self, size, closure, material):
        self.size = size                            #для нагрудного кармана, в два сложения, в три сложения, зажимы для денег, кардхолдер
        self.closure = closure                      #классика, на кнопке, молния
        self.material = material                    #кожа, кожзаменитель

    def reliability(self):
        if {self.closure} == 'на кнопке' or {self.closure} == 'молния':
            print('Надёжность кошелька высокая')
        else:
            print('Надёжность кошелька оставляет желать лучшего')

    def coin_box(self):
        if {self.size} == 'для нагрудного кармана' \
                or {self.size} == 'в два сложения' \
                or {self.size} == 'в три сложения':
            print('В данном кошельке есть монетница')
        else:
            print('В данном кошельке нет монетницы')


class Headphones:
    def __init__(self, brand, country, typeph):
        self.brand = brand
        self.country = country
        self.typeph = typeph

    def micro(self):
        print('Наушники снабжены встроенным микрофоном')

    def kind(self):
        print('Вид наушника - вкладыш')


class Book:
    def __init__(self, author, publication, edit_num, genre, booktype):
        self.author = author
        self.publication = publication
        self.edit_num = edit_num
        self.genre = genre
        self.booktype = booktype

    def book_kind(self):
        print('Эта книга печатная')             #электронная, печатная

    def book_type(self):
        print(f"Эта книга {self.genre} жанра {self.booktype}")


class Copybook:
    def __init__(self, copybtype, copybsize, copybformat):
        self.copebtype = copybtype
        self.copybsize = copybsize
        self.copybformat = copybformat

    def capacity(self):
        print(f"В тетради {self.copybsize} листов")

    def form(self):
        print(f"Тетрадь формата {self.copybformat}")



#задача 2
class Car:
    def __init__(self, brand, model, issueyear):
        self.brand = brand
        self.model = model
        self.issueyear = issueyear
        self.speed = 0

    def up_speed(self):
        self.speed += 5

    def down_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def current_speed(self):
        print(f"текущая скорость {self.speed}")

    def slew_speed(self):
        self.speed = - self.speed



#задача 3
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f"Привет, меня зовут {self.name}")

    def say_age(self):
        print(f"Мне {self.age} лет")

class Doctor(Human):

    def __init__(self, name, age, speciality, experience, salary, workplace, studyplace, qualification, position):
        super().__init__(name, age)
        self.speciality = speciality
        self.experience = experience
        self.salary = salary
        self.workplace = workplace
        self.studyplace = studyplace
        self.qualification = qualification
        self.position = position




    def do(self):
        print(f"Следую протоколу оказания мед. помощи")

    def work(self):
        print(f"я работаю в {self.workplace}, у меня стаж {self.experience} лет")