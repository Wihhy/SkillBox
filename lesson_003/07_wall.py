# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


start_x = simple_draw.get_point(0, 0)
start_y = simple_draw.get_point(100, 50)
i = 1
bricks_positions_x = (
    (simple_draw.get_point(0, 0)),
    {0: 100},
    {0: 200},
    {0: 300},
    {0: 400},
    {0: 500},
    {0: 600}
)
bricks_positions_y = (
    (simple_draw.get_point(100, 50)),
    {200: 50},
    {300: 50},
    {400: 50},
    {500: 50},
    {600: 50},
    {700: 50}
)
for x in bricks_positions_x:
    for y in bricks_positions_y:
        left_bottom = bricks_positions_x[x]

        simple_draw.rectangle(x, y)
simple_draw.pause()
