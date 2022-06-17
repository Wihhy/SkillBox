import simple_draw as sd

# sd.resolution = (1500, 800)


def ground():
    start = sd.get_point(x=0, y=0)
    end = sd.get_point(x=sd.resolution[0], y=100)
    sd.rectangle(left_bottom=start, right_top=end, color=sd.COLOR_DARK_GREEN)


sd.pause()
