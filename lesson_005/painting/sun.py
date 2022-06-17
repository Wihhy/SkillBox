import simple_draw as sd

point = sd.get_point(x=300, y=300)


def sun(center_point, size):
    sd.circle(center_position=center_point, radius=50*size, width=2)
    angle = -30
    v1 = sd.get_vector(start_point=center_point, angle=angle + 30, length=25*size, width=2)
    while angle < 361:
        v2 = sd.get_vector(start_point=center_point, angle=angle + 30, length=50 * size, width=2)
        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 30, length=45 * size, width=2)
        v3.draw()
        angle += 30


sun(center_point=point, size=1.3)

sd.pause()
