# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    center = sd.get_point(x=x, y=y)
    sd.circle(center_position=center, color=color, radius=50, width=2)  # Head
    left_eye = sd.get_point(x=x-20, y=y+10)
    sd.circle(center_position=left_eye, radius=5, color=color, width=2)  # Left eye
    right_eye = sd.get_point(x=x + 20, y=y + 10)
    sd.circle(center_position=right_eye, radius=5, color=color, width=2)  # Right eye
    nose = sd.get_point(x=x, y=y-8)
    sd.circle(center_position=nose, radius=2, color=color, width=2)  # Nose
    left_corner = sd.get_point(x=x-25, y=y-20)
    mouth_center1 = sd.get_point(x=x-15, y=y-30)
    mouth_center2 = sd.get_point(x=x+15, y=y-30)
    right_corner = sd.get_point(x=x+25, y=y-20)
    mouth = [left_corner, mouth_center1, mouth_center2, right_corner]
    sd.lines(mouth, color=color, width=2)


smile(300, 300, sd.COLOR_GREEN)



sd.pause()
