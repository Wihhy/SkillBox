import simple_draw as sd
sd.resolution = (1500, 800)
x = 0
y = 0
brick_length = 50
brick_height = 25

first_roof_point = sd.get_point(x=x - brick_length * 0.5, y=y + brick_height * 12)
second_roof_point = sd.get_point(x=x + brick_length * 6, y=y + brick_height * 12)
thirst_roof_point = sd.get_point(x=x + brick_length * 3, y=y + brick_height * 16)
roof = [first_roof_point, second_roof_point, thirst_roof_point]
sd.polygon(roof, width=0, color=sd.COLOR_DARK_ORANGE)

sd.pause()
