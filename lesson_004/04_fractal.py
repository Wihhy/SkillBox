# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

point_0 = sd.get_point(600, 5)
angle_0 = 90
length_0 = 150

#
# def branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=90, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle - 30, length=length * 0.8, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v1.end_point, angle=angle + 30, length=length * 0.8, width=3)
#     v3.draw()
#
#
# branches(point=point_0, angle=angle_0, length=length_0)


# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * 0.7
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


# for delta in range(10, 51, 10):
#     branch(point=point_0, angle=angle_0, length=length_0, delta=delta)
# for delta in range(-50, 0, 10):
#     branch(point=point_0, angle=angle_0, length=length_0, delta=delta)

# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * 0.7
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * 0.7
# next_point = branch(point=next_point, angle=next_angle, length=next_length)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
# v1 = sd.get_vector(start_point=point_0, angle=90, length=length_0, width=3)
# v1.draw()
#
#
# def branches(point, angle, length):
#     v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length * 0.8, width=3)
#     v2.draw()
#     if length < 10:
#         return
#     v3 = sd.get_vector(start_point=point, angle=angle + 30, length=length * 0.8, width=3)
#     v3.draw()
#     if length < 10:
#         return
#     branches(point=v2.end_point, angle=angle - 30, length=length * 0.75)
#     branches(point=v3.end_point, angle=angle + 30, length=length * 0.75)
#
#
# branches(point=v1.end_point, angle=angle_0, length=length_0)
# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


v1 = sd.get_vector(start_point=point_0, angle=90, length=length_0, width=3)
v1.draw()


def branches(point, angle, length):
    v2 = sd.get_vector(start_point=point, angle=angle - sd.random_number(10, 42),
                       length=length * round(random.uniform(0.6, 0.95), 2), width=3)
    v2.draw()
    if length < 5:
        return
    v3 = sd.get_vector(start_point=point, angle=angle + sd.random_number(10, 42),
                       length=length * round(random.uniform(0.6, 0.95), 2), width=3)
    v3.draw()
    if length < 5:
        return
    branches(point=v2.end_point, angle=angle - 30, length=length * 0.75)
    branches(point=v3.end_point, angle=angle + 30, length=length * 0.75)


branches(point=v1.end_point, angle=angle_0, length=length_0)


# Пригодятся функции
# sd.random_number()

sd.pause()


