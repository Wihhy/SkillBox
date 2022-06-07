# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

color_dict = \
    {0: 'COLOR_RED',
     1: 'COLOR_ORANGE',
     2: 'COLOR_YELLOW',
     3: 'COLOR_GREEN',
     4: 'COLOR_CYAN',
     5: 'COLOR_BLUE',
     6: 'COLOR_PURPLE'
     }
print(color_dict,)
print('Введите номер желаемого цвета:')
color_input = int(input())
dot = sd.get_point(300, 300)
i = 0
for i in color_dict:
    if i == color_input:
        color = color_dict[i]
        i += 1


def draw(point, length, range_cycle, angle_value, color):
    angle = 0
    for cycle in range(range_cycle):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        point = v1.end_point
        angle += angle_value
        sd.line(start_point=v1.start_point, end_point=v1.end_point, width=4, color=color)
        v1.draw()


draw(point=dot, length=100, range_cycle=4, angle_value=90, color=color)
sd.pause()
