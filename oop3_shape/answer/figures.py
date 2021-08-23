from shape import Shape
from plot import PlotObject
import math

class Point(Shape, PlotObject):
    id = None
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return 0

    def move(self, to_x, to_y):
        self.x += to_x
        self.y += to_y

    def display(self, canvas):
        self.id = canvas.create_oval(*self.__get_points())

    def __get_points(self):
        x1 = self.x - 1
        y1 = self.y - 1
        x2 = self.x + 1
        y2 = self.y + 1
        return x1, y1, x2, y2


class Rectangle(Shape, PlotObject):
    '''
    가로가 x축과 평행한 직사각형
    '''
    id = None
    point = None
    height, width = 0, 0

    def __init__(self, x, y, h1, w1):
        self.point = Point(x, y)
        self.height = h1
        self.width = w1

    def calculate_area(self):
        return self.height * self.width

    def move(self, to_x, to_y):
        self.point.move(to_x, to_y)

    def display(self, canvas):
        self.id = canvas.create_rectangle(*self.__get_points())

    def __get_points(self):
        x1 = self.point.x
        y1 = self.point.y
        x2 = self.point.x + self.width
        y2 = self.point.y + self.height
        return x1, y1, x2, y2


class Circle(Shape, PlotObject):
    id = None
    center = None
    radius = 0

    def __init__(self, x, y, r):
        self.center = Point(x, y)
        self.radius = r

    def calculate_area(self):
        return math.pi * pow(self.radius, 2)

    def move(self, to_x, to_y):
        self.center.move(to_x, to_y)

    def display(self, canvas):
        self.id = canvas.create_oval(*self.__get_points())

    def __get_points(self):
        x1 = self.center.x - self.radius
        y1 = self.center.y - self.radius
        x2 = self.center.x + self.radius
        y2 = self.center.x + self.radius
        return x1, y1, x2, y2


class RegularTriangle(Shape, PlotObject):
    '''
    한 변이 x축과 평행한 정삼각형
    '''
    id = None
    point = None
    side = 0

    def __init__(self, x, y, s):
        self.point = Point(x, y)
        self.side = s

    def calculate_area(self):
        return (math.sqrt(3) / 4) * pow(self.side, 2)

    def move(self, to_x, to_y):
        self.point.move(to_x, to_y)

    def display(self, canvas):
        self.id = canvas.create_polygon(*self.__get_points())

    def __get_points(self):
        x1 = self.point.x
        y1 = self.point.y
        x2 = self.point.x + self.side
        y2 = y1
        x3 = self.point.x + 0.5 * self.side
        y3 = self.point.y + 0.5 * math.sqrt(3) * self.side
        return x1, y1, x2, y2, x3, y3









