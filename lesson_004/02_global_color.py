# -*- coding: utf-8 -*-
import simple_draw as sd
from pprint import pprint
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

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)
dark_yellow = (127, 127, 0)
green = (0, 127, 0)
dark_cyan = (0, 127, 127)
dark_blue = (0, 0, 127)
dark_purple = (127, 0, 127)

color_dict = {
    **{0: red},
    **{1: green},
    **{2: white},
    **{3: black},
    **{4: orange},
    **{5: yellow},
    **{6: cyan},
    **{7: blue},
    **{8: purple},
    **{9: dark_yellow},
    **{10: dark_cyan},
    **{11: dark_blue},
    **{12: dark_purple}
}

color_list = [
    '0: red',
    '1: green',
    '2: white',
    '3: black',
    '4: orange',
    '5: yellow',
    '6: cyan',
    '7: blue',
    '8: purple',
    '9: dark_yellow',
    '10: dark_cyan',
    '11: dark_blue',
    '12: dark_purple',
]

dot = sd.get_point(300, 300)

pprint(color_list)

print('Введите номер желаемого цвета:')
color_input = int(input())

print('Введите желаемое количество углов в фигуре:')
number_of_corners = int(input())
if number_of_corners > 0:
    print('Введите угол в желаемой фигуре:')
    angle_value = float(input())

print('Введите длинну сторон в желаемо фигуре:')
side_length = float(input())


def draw(point, length=side_length, number_of_corners=number_of_corners, angle_value=angle_value, color=yellow):
    angle = 0
    if number_of_corners == 0:
        sd.circle(center_position=point, radius=side_length, color=color, width=4)
    for cycle in range(number_of_corners):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        point = v1.end_point
        angle += angle_value
        sd.line(start_point=v1.start_point, end_point=v1.end_point, width=4, color=color)
        v1.draw()


for i in color_dict:
    if i == color_input:
        color = color_dict[i]
        draw(point=dot, length=side_length, number_of_corners=number_of_corners, angle_value=angle_value, color=color)


sd.pause()
