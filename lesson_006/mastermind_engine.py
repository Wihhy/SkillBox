import random

# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

guessed_number = None
bulls = 0
cows = 0


def guessing_number():
    unic = False
    while unic is False:
        global guessed_number
        guessed_number = random.randint(1000, 9999)
        num1 = guessed_number // 1000
        num2 = (guessed_number % 1000) // 100
        num3 = (guessed_number % 100) // 10
        num4 = guessed_number % 10
        num_set = (num1, num2, num3, num4)
        if len(set(num_set)) == 4:
            unic = True
    return guessed_number


def check_number(guessed_number, checked_number):
    gues1 = guessed_number // 1000
    gues2 = (guessed_number % 1000) // 100
    gues3 = (guessed_number % 100) // 10
    gues4 = guessed_number % 10
    gues_set = (gues1, gues2, gues3, gues4)

    user1 = checked_number // 1000
    user2 = (checked_number % 1000) // 100
    user3 = (checked_number % 100) // 10
    user4 = checked_number % 10
    user_set = (user1, user2, user3, user4)
    for i in gues_set:
        for j in user_set:
            if j == i:
                global cows
                cows += 1
    gues = 0
    user = 0

    for k in range(4):
        for n in range(4):
            if gues == user:
                if gues_set[gues] == user_set[user]:
                    global bulls
                    bulls += 1
                    # cows = cows - 1
            user += 1
        user = user - 4
        gues += 1
    cows = cows - bulls
    animals = {'bulls': bulls, 'cows': cows}
    bulls = 0
    cows = 0
    return animals


# check_number(guessed_number=2749, checked_number=2749)
# print(f'korovi: {cows}, biki: {bulls}')
