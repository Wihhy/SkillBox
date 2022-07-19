# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
from pprint import pprint


class LogParser:

    def __init__(self, file_for_pars_name):
        self.file_name = file_for_pars_name
        self.stat = {}

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 10:
            raise StopIteration
        return self.stat

    def pars(self):
        with open(self.file_name, encoding='utf8', mode='r') as file:
            for line in file:
                if 'NOK' in line:
                    event_time = line[1:17]
                    if event_time in self.stat:
                        self.stat[event_time] += 1
                    else:
                        self.stat[event_time] = 1


# def get_out_TXT(self, file_for_out_name):
# with open(file=file_for_out_name, encoding='utf8', mode='w') as file:
#     for i in self.stat:
#         file.writelines(f'[{i}] {self.stat[i]}\n')


parser = LogParser(file_for_pars_name='events.txt')
parser.pars()
with open(file='out.txt', encoding='utf8', mode='a') as file:
    for list in parser:
        for time in list:
            pprint(time)
        # pprint(time)
        # file.writelines(f'[{time}] {event}\n')
# parser.get_out_TXT(file_for_out_name='out.txt')
