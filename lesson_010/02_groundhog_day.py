# -*- coding: utf-8 -*-
from random import randint, choice
from termcolor import cprint
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class StrMainClass(Exception):

    def __init__(self):
        super().__init__()
        self.massage = None

    def __str__(self):
        return self.massage


class IamGodError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Режим Бога!'


class DrunkError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Нахуярился в говнище!'


class CarCrashError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Разъебался на машине!'


class GluttonyError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Обожрался к хуям!'


class DepressionError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Впал в депрессию!☹'


class SuicideError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.massage = f'Выпилился нахуй!'


def one_day(total_carma):
    incidents = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
    carma = randint(1, 7)
    probability = randint(1, 13)
    if probability == 13:
        incident = choice(incidents)
        raise incident
    else:
        total_carma += carma
    return total_carma


def write_to_log(line):
    with open(file='groundhog_day_log', mode='a', encoding='utf8') as file:
        file.write(line)


if __name__ == '__main__':
    day = 1
    total_carma = 0
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            cprint(f'{"=" * 10}День {day}{"=" * 10}', color='cyan')
            total_carma = one_day(total_carma=total_carma)
            cprint(f'Карма - {total_carma}', color='green')
            day += 1
        except StrMainClass as exc:
            line = f'Произошёл инцидент: {exc} На {day} дне!\n'
            write_to_log(line=line)
            print(line)

