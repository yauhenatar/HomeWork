class Horse():

    population = 0

    def __init__(self, hooves, color, breed, name):
        self.hooves = hooves
        self.color = color
        self.breed = breed
        self.name = name
        Horse.population += 1

    def nicker(self):
        print(f'{self.name} восклицает: "И-го-го"')

    def hop(self):
        from random import randint
        return print(f'{self.name} срывается с места и скачет со скоростью {randint(15, 89)} км/ч')

    def eat(self):
        print(f'{self.name} видит яблоко и кушает его')

plotva = Horse(4, 'brown', 'Altai', 'Plotva')
plotva.nicker()
plotva.hop()
plotva.eat()