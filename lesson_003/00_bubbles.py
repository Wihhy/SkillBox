# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(600, 300)
# sd.circle(center_position=point)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=1)

# point = sd.get_point(600, 300)
# bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 300)
#     bubble(point=point, step=10)


# Нарисовать три ряда по 10 пузырьков

# for y in range(10, 250, 10):
#     for x in range(10, 1200, 10):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=3)
sd.pause()


