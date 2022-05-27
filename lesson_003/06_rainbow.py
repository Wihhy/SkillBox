# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x1 = 45
y1 = 45
x2 = 350
y2 = 450
for i in rainbow_colors:
    start_point = sd.get_point(x=x1, y=y1)
    end_point = sd.get_point(x=x2, y=y2)
    sd.line(start_point=start_point, end_point=end_point, width=5, color=i)
    x1 += 5
    x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, чтобы было красиво


# point = sd.get_point(300, -100)
# radius = 300
# for i in rainbow_colors:
#     sd.circle(point, radius=radius, color=i, width=40)
#     radius += 40



sd.pause()
