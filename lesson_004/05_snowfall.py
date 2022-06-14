# -*- coding: utf-8 -*-

import simple_draw as sd
import random


sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

N = 20

y_list = [500, 490, 480, 400, 440]
x_list = [100, 110, 120, 130]
length_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 15, 25, 35, 45, 55, 65, 75, 85, 95]
print()

y = random.choice(y_list)
x = random.choice(x_list)

y2 = random.choice(y_list)
x2 = random.choice(x_list)


length1 = random.choice(length_list)
length2 = random.choice(length_list)


while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=length1)
    y -= 10
    if y < 50:
        break
    x = x * round(random.uniform(1.15, 0.95), 2)

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=length2)
    y2 -= 10
    if y2 < 50:
        break
    x2 = x2 * round(random.uniform(1.15, 0.95), 2)

    sd.sleep(0.07)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
