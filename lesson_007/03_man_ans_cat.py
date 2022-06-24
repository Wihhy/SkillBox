# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class House:

    def __init__(self):
        self.dirt = 0
        self.bowl_for_food = 0
        self.cat_food = 20
        self.human_food = 10


class Cat:

    def __init__(self, name):
        self.satiety = 10
        self.name = name

    def eat(self):
        if house.cat_food >= 20:
            _food = randint(8, 12)
            self.satiety += _food
            house.bowl_for_food -= _food
            house.dirt += _food
            print(f'{self.name} поел')
        else:
            print(f'Еды у {self.name} нет')

    def sleep(self):
        _hanger = randint(4, 8)
        self.satiety -= _hanger
        print(f'{self.name} весь день спал')

    def play(self):
        self.satiety -= randint(4, 8)
        house.dirt += randint(8, 12)
        print(f'{self.name} драл обои')

    def act(self):
        if self.satiety <= 0:
            print(f'{self.name} умер..')
            quit()
        else:
            dice = randint(0, 4)
            if self.satiety < 10:
                self.eat()
            elif dice == 2:
                self.play()
            elif dice == 0:
                self.eat()
            else:
                self.sleep()

    def __str__(self):
        return f'Я {self.name}, сытость - {self.satiety}'


class Human:

    def __init__(self, name):
        self.money = 50
        self.satiety = 10
        self.name = name

    def eat(self):
        if house.human_food >= 1:
            _food = randint(8, 12)
            self.satiety += _food
            house.human_food -= _food
            house.dirt += randint(2, 4)
            print(f'{self.name} поел')
        else:
            print(f'Еды у {self.name} нет')
            self.shopping_forself()

    def work(self):
        self.money += 60
        self.satiety -= 15
        print(f'{self.name} сходил на работу')

    def clean(self):
        house.dirt -= 30
        self.satiety -= randint(6, 10)
        print(f'{self.name} убрался дома')

    def shopping_forself(self):
        house.human_food += 80
        self.money -= 40
        self.satiety -= randint(3, 5)
        print(f'{self.name} сходил в магазин по еду себе')

    def shopping_for_cat(self):
        house.cat_food += 80
        self.money -= 40
        self.satiety -= randint(3, 5)
        print(f'{self.name} сходил в магазин по еду коту')

    def __str__(self):
        return f'Я {self.name}, сытость - {self.satiety}, деньги - {self.money}'

    def play(self):
        self.satiety -= randint(5, 15)
        print(f'{self.name} играл весь день')

    def act(self):
        if self.satiety <= 0:
            print(f'{self.name} умер...')
            quit()
        dice = randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif house.dirt > 80:
            self.clean()
        elif house.human_food < 30:
            self.shopping_forself()
        elif house.cat_food < 30:
            self.shopping_for_cat()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


house = House()
masyanya = Human(name='Масяня')
dimok = Cat(name='кот Дымок')
viktor = Cat(name='кот Виктор')
avgustii = Cat(name='кот Августий')

for day in range(1, 366):
    print(f'================ день {day} ==================')
    masyanya.act()
    dimok.act()
    viktor.act()
    avgustii.act()

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
