# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1200, 700)
start_x = 0
start_y = 0


for j in range(12):
    start_point = sd.get_point(x=0, y=start_y)
    end_point = sd.get_point(x=600, y=start_y)
    sd.line(start_point, end_point, color=sd.COLOR_YELLOW, width=2)
    start_y += 50

    for i in range(6):
        vertical_start_point = sd.get_point(x=start_x + 100, y=start_y + 50)
        vertical_end_point = sd.get_point(x=start_x + 100, y=start_y)
        sd.line(start_point=vertical_start_point, end_point=vertical_end_point, color=sd.COLOR_YELLOW, width=2)
        start_x += 100
        if start_x > 600:
            break

        for k in range(6):
            vertical_start_point2 = sd.get_point(x=start_x - 50, y=start_y)
            vertical_end_point2 = sd.get_point(x=start_x - 50, y=start_y - 50)
            sd.line(start_point=vertical_start_point2, end_point=vertical_end_point2, color=sd.COLOR_YELLOW, width=2)
            start_x += 100
            if start_x > 600:
                break
        start_x = start_x - 600
    start_x = start_x - 550





sd.pause()




