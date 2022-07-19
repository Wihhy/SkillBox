# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw(start_point, angle, side_length):
        angle_value = 360 / n
        for cycle in range(n):
            v1 = sd.get_vector(start_point=start_point, angle=angle, length=side_length, width=1)
            angle += angle_value
            sd.line(start_point=v1.start_point, end_point=v1.end_point, width=4)
            v1.draw()

    return draw


draw_triangle = get_polygon(n=3)
draw_triangle(start_point=sd.get_point(200, 200), angle=13, side_length=100)


sd.pause()
