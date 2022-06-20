# -*- coding: utf-8 -*-

import simple_draw as sd
import random


sd.resolution = (1500, 800)

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

snowflake_count = 20
snowflake_list = []
snowflake_length_list = []

for i in range(snowflake_count):
    snowflake_list.append(random.randint(0, 1500))
    snowflake_list.append(random.randint(800, 900))
    snowflake_length_list.append(random.randint(10, 100))


while True:
    sd.start_drawing()
    for number in range(0, snowflake_count, 2):
        y = snowflake_list[number + 1]
        point = sd.get_point(snowflake_list[number], y)
        sd.snowflake(center=point, length=100, )
        y -= 10
        if y < 100:
            del snowflake_list[number]
            del snowflake_list[number + 1]
            print(len(snowflake_list))
            snowflake_list.append(random.randint(0, 1500))
            snowflake_list.append(random.randint(800, 900))
            break
        snowflake_list[number + 1] = y
        sd.finish_drawing()
        # sd.sleep(0.01)
        sd.snowflake(center=point, length=100, color=sd.background_color)
    if sd.user_want_exit():
        break



    # point = sd.get_point(x, y)
    # sd.snowflake(center=point, length=length1)
    # y -= 10
    # if y < 50:
    #     break
    # x = x * round(random.uniform(1.15, 0.95), 2)
    #
    # point2 = sd.get_point(x2, y2)
    # sd.snowflake(center=point2, length=length2)
    # y2 -= 10
    # if y2 < 50:
    #     break
    # x2 = x2 * round(random.uniform(1.15, 0.95), 2)
    #
    # sd.sleep(0.07)
    # if sd.user_want_exit():
    #     break

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
