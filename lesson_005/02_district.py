# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks
citizens = []
citizens.extend(folks)
from district.central_street.house1.room2 import folks
citizens.extend(folks)

from district.central_street.house2.room1 import folks
citizens.extend(folks)
from district.central_street.house2.room2 import folks
citizens.extend(folks)

from district.soviet_street.house1.room1 import folks
citizens.extend(folks)
from district.soviet_street.house1.room2 import folks
citizens.extend(folks)

from district.soviet_street.house2.room1 import folks
citizens.extend(folks)
from district.soviet_street.house2.room2 import folks
citizens.extend(folks)

print(*citizens, sep=', ')





