# -*- coding: utf-8 -*-
import zipfile
import os
import shutil
import datetime

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

path = os.path.normpath('E:\\PyCharm Projects\\course\\lesson_009\\icons')
destination = os.path.normpath('E:\\PyCharm Projects\\course\\lesson_009\\Here\\')
years = []
months = []
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        file_time = datetime.datetime(os.path.getmtime(filename=full_path))
        # print(dirpath, file, file_time, sep='\n')
        # shutil.move(src=full_path, dst=destination)
        years.append(file_time[0])
        months.append(file_time[1])

years_set = set(years)
months_set = set(months)
for year in years_set:
    if not os.path.exists(f'{destination}\\{year}'):
        os.mkdir(f'{destination}\\{year}')

    for month in months_set:
        if not os.path.exists(f'{destination}\\{year}\\{month}'):
            os.mkdir(f'{destination}\\{year}\\{month}')


print(f'{years}\n{years_set}\n{months}\n{months_set}')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# class ZipOperations:
#     __name = None
#
#     def __init__(self, file_name, output_path):
#         self.set_file_name(file_name)
#         self.copy_files_from_zip(output_path)
#         self.read_file = None
#
#     def set_file_name(self, file_name):
#         self.__name = file_name
#
#     def get_file_name(self):
#         return self.__name
#
#     def zip_file(self):
#         return zipfile.ZipFile(self.get_file_name(), mode='r')
#
#     def copy_files_from_zip(self, output_path):
#
#         with self.zip_file() as zf:
#             for file in zf.infolist():
#                 path = zipfile.Path(zf, file.filename)
#                 if path.is_file():
#                     date = datetime.datetime(*file.date_time)
#                     output_dir = os.path.join(output_path, str(date.year), str(date.month))
#                     output_file_name = os.path.join(output_dir, path.name)
#                     if not os.path.exists(output_dir):
#                         os.makedirs(output_dir)
#                     with open(output_file_name, 'wb') as f:
#                         f.write(path.read_bytes())
#
#
# Open_file = ZipOperations(file_name='icons.zip', output_path='Result')
