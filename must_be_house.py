import simple_draw as sd

sd.resolution = (1400, 800)


def house(x, y, brick_height, brick_length):
    start_x = x
    start_y = y
    for j in range(12):
        start_point = sd.get_point(x=start_x, y=start_y)
        end_point = sd.get_point(x=start_x + brick_length * 6, y=start_y)
        sd.line(start_point, end_point, color=sd.COLOR_ORANGE, width=2)
        start_y += brick_height

        for i in range(6):
            vertical_start_point = sd.get_point(x=start_x, y=start_y)
            vertical_end_point = sd.get_point(x=start_x, y=start_y + brick_height)
            sd.line(start_point=vertical_start_point, end_point=vertical_end_point, color=sd.COLOR_ORANGE, width=2)
            start_x += brick_length
            if start_x > (x + brick_length * 6):
                start_x = start_x - brick_height * 6
                break

            for k in range(6):
                vertical_start_point2 = sd.get_point(x=start_x, y=start_y)
                vertical_end_point2 = sd.get_point(x=start_x, y=start_y + brick_height)
                sd.line(start_point=vertical_start_point2, end_point=vertical_end_point2, color=sd.COLOR_ORANGE, width=2)
                start_x += brick_length
                if start_x > (x + brick_length * 6):
                    start_x = start_x - brick_length * 7
                    break

    first_roof_point = sd.get_point(x=x-brick_length * 0.5, y=y + brick_height * 12)
    second_roof_point = sd.get_point(x=x + brick_length * 6 + brick_length * 0.5, y=y + brick_height * 12)
    thirst_roof_point = sd.get_point(x=x + brick_length * 3, y=y + brick_height * 16)
    roof = [first_roof_point, second_roof_point, thirst_roof_point]
    sd.polygon(roof, width=0, color=sd.COLOR_DARK_ORANGE)


house(x=500, y=150, brick_height=25, brick_length=50)

sd.pause()
