import simple_draw as sd
sd.resolution = (1500, 800)


def rainbow(x, y, radius, width):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    point = sd.get_point(x=x, y=y)
    radius = radius
    for i in rainbow_colors:
        sd.circle(point, radius=radius, color=i, width=width)
        radius += width


rainbow(x=0, y=-400, radius=1600, width=20)

sd.pause()
