# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class CharCounter:

    def __init__(self, file_name):
        self.stat = {}
        self.file_name = file_name

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def count(self):
        char_totals = 0
        with open('voyna-i-mir.txt', mode='r', encoding='cp1251') as text:
            for line in text:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
        # pprint(self.stat)
        print(f'+{"-" * 9}+{"-" * 9}+''\n'
              f'|  буква  | частота |''\n'
              f'+{"-" * 9}+{"-" * 9}+')
        for item in self.stat:
            print(f'|{item:^9}|{self.stat[item]:^9}|')
            char_totals += self.stat[item]
        print(f'+{"-" * 9}+{"-" * 9}+''\n'
              f'|  итого  |{char_totals:^9}|''\n'
              f'+{"-" * 9}+{"-" * 9}+''\n')


char_stat = CharCounter(file_name='E:\\PyCharm Projects\\course\\lesson_009\\python_snippets\\voyna-i-mir.txt.zip')
char_stat.unzip()
char_stat.count()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
