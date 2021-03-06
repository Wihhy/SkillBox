# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# print(get_prime_numbers(10000))
# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых объектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
from pprint import pprint


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        list = self.get_prime_numbers()
        for i in list:
            # print(f'{i}')
            print(i)
        raise StopIteration

    def get_prime_numbers(self):
        self.prime_numbers = []
        for number in range(2, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
        return self.prime_numbers


prime_number_iterator = PrimeNumbers(n=10000)
for guessed_number in prime_number_iterator:
    print(guessed_number)


# TODO после подтверждения части 1 преподавателем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     pass
#     # TODO здесь ваш код
#
#
# for guessed_number in prime_numbers_generator(n=10000):
#     print(guessed_number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном понимании - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например - 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
