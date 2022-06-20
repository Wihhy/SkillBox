# import simple_draw as sd
# sd.resolution = (1500, 800)
# x = 0
# y = 0
# brick_length = 50
# brick_height = 25
#
# first_roof_point = sd.get_point(x=x - brick_length * 0.5, y=y + brick_height * 12)
# second_roof_point = sd.get_point(x=x + brick_length * 6, y=y + brick_height * 12)
# thirst_roof_point = sd.get_point(x=x + brick_length * 3, y=y + brick_height * 16)
# roof = [first_roof_point, second_roof_point, thirst_roof_point]
# sd.polygon(roof, width=0, color=sd.COLOR_DARK_ORANGE)
#
# sd.pause()
# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd
import random

sd.set_screen_size(width=1200, height=800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
list_coordinates = []
length_snow = []
abc_list = []

fallen_list = []
snowflakes_fallen_lengths = []
abc_list_fallen = []

for counter in range(N):
    list_coordinates.append([sd.random_number(100, 1200), sd.random_number(800, 1300)])
    length_snow.append(sd.random_number(20, 70))
    abc_list.append([round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2), sd.random_number(50, 70)])

print(list_coordinates)
print(length_snow)
print(abc_list)

while True:
    for i in range(N):
        point = sd.get_point(list_coordinates[i][0], list_coordinates[i][1])
        sd.start_drawing()
        sd.snowflake(center=point, length=length_snow[i], color=sd.background_color, factor_a=abc_list[i][0],
                     factor_b=abc_list[i][1], factor_c=abc_list[i][2])

        if list_coordinates[i][1] >= length_snow[i]:
            list_coordinates[i][1] -= sd.randint(20, 40)
            left_or_right_rand = sd.randint(0, 2)
            if left_or_right_rand < 0.5:
                list_coordinates[i][0] -= sd.randint(7, 10)
            else:
                list_coordinates[i][0] += sd.randint(7, 10)

            point2 = sd.get_point(list_coordinates[i][0], list_coordinates[i][1])
            sd.snowflake(center=point2, length=length_snow[i], color=sd.COLOR_WHITE, factor_a=abc_list[i][0],
                         factor_b=abc_list[i][1], factor_c=abc_list[i][2])

        else:
            fallen_list.append([list_coordinates[i][0], list_coordinates[i][1]])
            snowflakes_fallen_lengths.append(length_snow[i])
            abc_list_fallen.append(
                [abc_list[i][0], abc_list[i][1], abc_list[i][2]])
            snowflakes_fallen_lengths.append(length_snow[i])

            list_coordinates.pop(i)
            length_snow.pop(i)
            abc_list.pop(i)

            length_snow.append(sd.random_number(20, 70))
            list_coordinates.append([sd.randint(0, 1200), 800 + 50])
            abc_list_fallen.append([round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2),
                                    sd.random_number(50, 70)])

        for i in range(len(fallen_list)):
            point = sd.get_point(fallen_list[i][0], fallen_list[i][1])
            sd.snowflake(center=point, length=snowflakes_fallen_lengths[i], color=sd.COLOR_WHITE,
                         factor_a=abc_list[i][0], factor_b=abc_list[i][1], factor_c=abc_list[i][2])

        sd.finish_drawing()
        sd.sleep(0.01)
        if sd.user_want_exit():
            break
