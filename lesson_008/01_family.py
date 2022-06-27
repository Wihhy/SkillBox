# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30


    def __str__(self):
        return f'В доме {self.money} денег, {self.food} еды, {self.dirt} грязи'


class Husband:

    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.father_play = 0
        self.father_eat = 0
        self.father_work = 0
        self.father_pet_cat = 0

    def __str__(self):
        return f'Батя {self.name}: сытость - {self.satiety}, счастье - {self.happiness}'

    def act(self):
        if self.satiety <= 0:
            cprint('Помер от голода')
            quit()
        elif self.happiness <= 10:
            print(f'Повесился от грусти(')
        elif self.satiety <= 30:
            self.eat()
        elif home.money <= 150:
            self.work()
        else:
            self.gaming()

    def eat(self):
        _food = randint(15, 30)
        self.satiety += _food
        home.food -= _food
        self.father_eat += 1
        cprint(f'Батя похавал', color='yellow')

    def work(self):
        self.satiety -= 10
        home.money += 150
        self.father_work += 1
        cprint(f'Батя сходил на работу', color='blue')

    def gaming(self):
        self.satiety -= 10
        self.happiness += 20
        self.father_play += 1
        cprint(f'Батя ебашил в дотку', color='green')

    def pet_the_cet(self):
        self.happiness += 5
        self.satiety -= 10
        cprint('Котик лащился к бате и он его погладил', color='green')
        self.father_pet_cat += 1


class Wife:

    def __init__(self, name):
        self.mom_cleans = 0
        self.mom_coats = 0
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.mom_rest = 0
        self.mom_eat = 0
        self.mom_shop = 0
        self.mom_pet_cat = 0

    def __str__(self):
        return f'Мать {self.name}: сытость - {self.satiety}, счастье - {self.happiness}'

    def act(self):
        if self.satiety <= 0:
            cprint('Померла от голода')
            quit()
        elif self.happiness <= 10:
            print(f'Повесилась от грусти(')
        elif self.satiety <= 30:
            self.eat()
        elif home.dirt >= 100:
            self.clean_house()
        elif home.money >= 500:
            self.buy_fur_coat()
        elif home.food <= 55:
            self.shopping_forself()
        elif home.cat_food <= 15:
            self.shopping_for_cat()
        elif self.happiness >= 100:
            self.rest()
        else:
            self.buy_fur_coat()

    def eat(self):
        _food = randint(10, 25)
        self.satiety += _food
        home.food -= _food
        self.mom_eat += 1
        cprint(f'Мать покушала', color='yellow')

    def shopping_forself(self):
        home.money -= 100
        home.food += 100
        self.satiety -= 10
        self.mom_shop += 1
        cprint(f'Мать сходила в магаз по хавку', color='magenta')

    def shopping_for_cat(self):
        home.money -= 100
        home.cat_food += 100
        self.satiety -= 10
        self.mom_shop += 1
        cprint(f'Мать сходила в магаз по хавку для кота', color='magenta')

    def buy_fur_coat(self):
        home.money -= 350
        self.happiness += 60
        self.satiety -= 10
        self.mom_coats += 1
        cprint(f'Мать прикупила пальто', color='red')

    def clean_house(self):
        home.dirt -= 100
        self.satiety -= 10
        self.mom_cleans += 1

    def rest(self):
        self.satiety -= 10
        self.mom_rest += 1

    def pet_the_cet(self):
        self.happiness += 5
        self.satiety -= 10
        self.mom_pet_cat += 1
        cprint('Котик лащился к матери и она его погладила', color='green')


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(1, 366):
#     serge.happiness -= 5
#     masha.happiness -= 5
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.cat_sleep = 0
        self.cat_play = 0
        self.cat_eat = 0
        self.name = name
        self.satiety = 10

    def __str__(self):
        return f'Котяра {self.name}: сытость - {self.satiety}'

    def act(self):
        if self.satiety <= 0:
            print('Кот сдох')
            quit()
        elif self.satiety <= 10:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.eat()
            elif dice == 2:
                self.play()
            elif dice == 3:
                serge.pet_the_cet()
            elif dice == 4:
                masha.pet_the_cet()
            else:
                self.sleep()

    def eat(self):
        _food = randint(5, 10)
        home.cat_food -= _food
        self.satiety += _food * 2
        self.cat_eat += 1
        cprint(f'Котяра похавал', color='yellow')

    def sleep(self):
        self.satiety -= 10
        cprint(f'Котяра дрых весь день', color='grey')
        self.cat_sleep += 1

    def play(self):
        self.satiety -= 10
        home.dirt += 5
        self.cat_play += 1
        cprint(f'Котяра подрал все обои', color='red')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name):
        self.child_sleep = 0
        self.child_eat = 0
        self.name = name
        self.satiety = 20
        self.happiness = 100

    def __str__(self):
        return f'Ребёнок {self.name}: сытость - {self.satiety}'

    def act(self):
        if self.satiety <= 0:
            print('Малой откинулся от голода')
            quit()
        elif self.satiety <= 10:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        _food = randint(6, 10)
        home.cat_food -= _food
        self.satiety += _food
        cprint(f'Малой похавал', color='yellow')
        self.child_eat += 1

    def sleep(self):
        self.satiety -= randint(4, 8)
        cprint(f'Малой проспал весь день', color='white')
        self.child_sleep += 1

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
dimok = Cat(name='Дымок')
for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.happiness -= 5
    masha.happiness -= 5
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    dimok.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(dimok, color='cyan')
    incident_probability = randint(1, 18)
    if incident_probability == 3:
        home.money = home.money // 2
        cprint('МИНУС БАБОСИКИ!!!', color='red')
    elif incident_probability == 5:
        home.food = home.food // 2
        home.cat_food = home.cat_food // 2
        cprint('МИНУС ХАВКА!!!', color='red')
print(f'Батя за год:\n'
      f'Играл {serge.father_play} раз, ходил на работу {serge.father_work} раз,'
      f' ел {serge.father_eat} раз, гладил кота {serge.father_pet_cat} раз\n'
      f'Мать за год:\n'
      f'Ела {masha.mom_eat} раз, ходила за покупками {masha.mom_shop} раз,'
      f' гладила кота {masha.mom_pet_cat} раз, убиралась в доме {masha.mom_cleans} раз,'
      f' отдыхала {masha.mom_rest} раз, купила {masha.mom_coats} пальто\n'
      f'Кот Мурзик за год:\n'
      f'Ел {murzik.cat_eat} раз, драл обои {murzik.cat_play} раз, спал {murzik.cat_sleep} раз\n'
      f'Кот Дымок за год:\n'
      f'Ел {dimok.cat_eat} раз, драл обои {dimok.cat_play} раз, спал {dimok.cat_sleep} раз\n'
      f'Малой за год:\n'
      f'Ел {kolya.child_eat} раз, спал {kolya.child_sleep} раз')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

