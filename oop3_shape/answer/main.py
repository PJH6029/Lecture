from plot import *
from figures import *
import time
import math
if __name__ == '__main__':
    painter = Painter(width=1000, height=250)

    group_center_x = 150
    group_center_y = 150
    r = 50
    h = 100
    w = 200

    pt1 = Point(group_center_x - r, group_center_y - r)
    pt2 = Point(group_center_x + r, group_center_y + r)
    pt3 = Point(group_center_x - r, group_center_y + r)
    pt4 = Point(group_center_x + r, group_center_y - r)
    rect = Rectangle(group_center_x - 0.5 * w, group_center_y - 0.5 * h, h, w)
    circle = Circle(group_center_x, group_center_y, r)
    reg_tri = RegularTriangle(group_center_x - 0.5 * r * math.sqrt(3), group_center_y - 0.5 * r, r * math.sqrt(3))

    painter.draw_many_objects(pt1, pt2, pt3, pt4, rect, circle, reg_tri)

    degree = 1
    for _ in range(1000):
        prev_radian = math.radians(degree - 1)
        radian = math.radians(degree)
        r = 20
        move_x = math.cos(radian) - math.cos(prev_radian)
        move_y = math.sin(radian) - math.sin(prev_radian)
        painter.move_object(pt1, pt2, pt3, pt4, rect, circle, reg_tri, to_x=r * move_x, to_y=r * move_y)

        time.sleep(0.01)
        degree += 1

    painter.show()

