# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exc:
    print(f'Введённое сообщение невозможно преобразовать в целое число, {exc}')
except IndexError as exc:
    print(f'Введено недостаточно символов!, {exc}')
except Exception as exc:
    print(f'Что то совсем непонятное: {exc}')


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

