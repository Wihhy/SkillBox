import simple_draw as sd
import random

sd.resolution = (1500, 800)


def tree(root_point, angle_0, length_0):
    v1 = sd.get_vector(start_point=root_point, angle=90, length=length_0, width=3)
    v1.draw()
    branches(point=v1.end_point, angle=angle_0, length=length_0)


def branches(point, angle, length):
    v2 = sd.get_vector(start_point=point, angle=angle - sd.random_number(10, 42),
                       length=length * round(random.uniform(0.6, 0.95), 2), width=3)
    v2.draw()
    if length < 5:
        return
    v3 = sd.get_vector(start_point=point, angle=angle + sd.random_number(10, 42),
                       length=length * round(random.uniform(0.6, 0.95), 2), width=3)
    v3.draw()
    if length < 5:
        return
    branches(point=v2.end_point, angle=angle - 30, length=length * 0.75)
    branches(point=v3.end_point, angle=angle + 30, length=length * 0.75)


sd.pause()
