# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogParser:

    def __init__(self, file_for_pars_name):
        self.file_name = file_for_pars_name
        self.stat = {}

    def pars(self):
        with open(self.file_name, encoding='utf8', mode='r') as file:
            for line in file:
                if 'NOK' in line:
                    event_time = line[1:17]
                    if event_time in self.stat:
                        self.stat[event_time] += 1
                    else:
                        self.stat[event_time] = 1

    def get_out_TXT(self, file_for_out_name):
        with open(file=file_for_out_name, encoding='utf8', mode='w') as file:
            for i in self.stat:
                file.writelines(f'[{i}] {self.stat[i]}\n')


parser = LogParser(file_for_pars_name='events.txt')
parser.pars()
parser.get_out_TXT(file_for_out_name='out.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
