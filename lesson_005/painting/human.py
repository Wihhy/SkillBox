import simple_draw as sd
sd.resolution = (1500, 800)


def body(center):
    out_head = sd.get_vector(start_point=center, angle=-90, length=50)
    chest = sd.get_vector(start_point=out_head.end_point, angle=-90, length=100, width=2)
    chest.draw()
    for_arms = sd.get_vector(start_point=out_head.end_point, angle=-90, length=20)
    left_arm = sd.get_vector(start_point=for_arms.end_point, angle=-130, length=50, width=2)
    left_arm.draw()
    left_arm = sd.get_vector(start_point=for_arms.end_point, angle=-50, length=50, width=2)
    left_arm.draw()
    left_leg = sd.get_vector(start_point=chest.end_point, angle=-130, length=50, width=2)
    left_leg.draw()
    left_leg = sd.get_vector(start_point=chest.end_point, angle=-50, length=50, width=2)
    left_leg.draw()


def smile(x, y, color):
    center = sd.get_point(x=x, y=y)
    sd.circle(center_position=center, color=color, radius=50, width=2)  # Head
    left_eye = sd.get_point(x=x-20, y=y+10)
    sd.circle(center_position=left_eye, radius=5, color=color, width=2)  # Left eye
    right_eye = sd.get_point(x=x + 20, y=y + 10)
    sd.circle(center_position=right_eye, radius=5, color=color, width=2)  # Right eye
    nose = sd.get_point(x=x, y=y-8)
    sd.circle(center_position=nose, radius=2, color=color, width=2)  # Nose
    left_corner = sd.get_point(x=x-25, y=y-20)
    mouth_center1 = sd.get_point(x=x-15, y=y-30)
    mouth_center2 = sd.get_point(x=x+15, y=y-30)
    right_corner = sd.get_point(x=x+25, y=y-20)
    mouth = [left_corner, mouth_center1, mouth_center2, right_corner]
    sd.lines(mouth, color=color, width=2)
    body(center=center)


smile(300, 300, sd.COLOR_YELLOW)








sd.pause()
