from shape import Shape
from plot import PlotObject
import math

# TODO 참고: 이 문제에서 좌표계는 왼쪽 위가 0, 0  /  x축은 오른쪽이 커지는 방향, y축은 왼쪽이 커지는 방향

class Point(Shape, PlotObject):
    id = None  # plot과 관련된 변수
    x, y = 0, 0

    def __init__(self, x, y):
        # TODO
        pass

    def calculate_area(self):
        return 0

    def move(self, to_x, to_y):
        # TODO
        # to_x, to_y만큼 도형을 이동, return 없음
        pass

    def display(self, canvas):
        self.id = canvas.create_oval(*self.__get_points())

    def __get_points(self):
        """
        점을 그리기 위한 좌표 정보 리턴

        return: (x1, y1, x2, y2)
        """
        # 점을 그리기 위한 좌표정보 리턴
        # 점을 반지름의 길이가 1인 원으로 표현
        # 왼쪽 위 꼭짓점과 오른쪽 아래 꼭짓점이 주어지면, 그 점으로 생성된 직사각형에 딱 맞는 원(타원)을 생성할 것임
        # TODO (이건 건드릴 필요x. 예시) x1, y1은 왼쪽 위, x2, y2는 오른쪽 아래

        pass


class Rectangle(Shape, PlotObject):
    """
    가로가 x축과 평행한 직사각형
    """
    id = None  # plot과 관련된 변수
    point = None  # 왼쪽 위 꼭짓점
    height, width = 0, 0  # 높이, 너비

    def __init__(self, x, y, h1, w1):
        # TODO 위치 정보를 Point의 객체로 self.point에 저장, 높이/너비는 변수에 저장
        pass

    def calculate_area(self):
        # TODO 넓이를 리턴
        pass

    def move(self, to_x, to_y):
        # TODO 직사각형을 to_x, to_y만큼 이동
        # Hint: 평행이동해도 height와 width는 변하지 x. 점만 이동하면 되는데, 관련 함수가 있나??
        pass

    def display(self, canvas):
        self.id = canvas.create_rectangle(*self.__get_points())

    def __get_points(self):
        """
        직사각형을 그리기 위한 좌표 정보 리턴

        return: (x1, y1, x2, y2)
        """
        # 직사각형은 왼쪽 위 꼭짓점, 오른쪽 아래 꼭짓점이 주어지면 그릴 수 있음
        pass


class Circle(Shape, PlotObject):
    id = None  # plot과 관련된 변수
    center = None  # 중심 point
    radius = 0  # 반지름

    def __init__(self, x, y, r):
        # TODO 위치 정보를 Point의 객체로 self.center에 저장, 반지름은 변수에 저장
        pass

    def calculate_area(self):
        # TODO 넓이 리턴
        pass

    def move(self, to_x, to_y):
        # TODO 원을 to_x, to_y만큼 이동
        # Hint: 평행이동해도 radius는 변하지 x. 점만 이동하면 되는데, 관련 함수가 있나??
        pass

    def display(self, canvas):
        self.id = canvas.create_oval(*self.__get_points())

    def __get_points(self):
        """
        원을 그리기 위한 좌표 정보 리턴

        return: (x1, y1, x2, y2)
        """
        # 원은 왼쪽 위 꼭짓점, 오른쪽 아래 꼭짓점이 주어지면 이로부터 생성된 직사각형에 딱 맞게 그릴 수 있음
        # Hint: Point의 __get_points() 참고 -> 반지름이 1인 경우임
        pass


class RegularTriangle(Shape, PlotObject):
    """
    한 변이 x축과 평행한 정삼각형
    """
    id = None  # plot과 관련된 변수
    point = None  # 왼쪽 위 꼭짓점
    side = 0  # 한 변의 길이

    def __init__(self, x, y, s):
        # TODO 위치 정보를 Point의 객체로 self.point에 저장, 변의 길이는 변수에 저장
        pass

    def calculate_area(self):
        # TODO 넓이 리턴
        pass

    def move(self, to_x, to_y):
        # TODO 정삼각형을 to_x, to_y만큼 이동
        # Hint: 평행이동해도 side는 변하지 x. 점만 이동하면 되는데, 관련 함수가 있나??
        pass

    def display(self, canvas):
        self.id = canvas.create_polygon(*self.__get_points())

    def __get_points(self):
        """
        정삼각형을 그리기 위한 좌표 정보 리턴

        return: (x1, y1, x2, y2, x3, y3)
        """
        # 삼각형은 세 점의 좌표를 모두 찍어줘야함
        # (x, y) 1, 2, 3의 순서는 중요하지 x (x3, y3, x2, y2, x1, y1) 등도 가능
        # 리턴할 때 x, y 쌍의 순서대로 리턴만 해주면 ok
        # Hint: self.point와 side를 알면 나머지 점들도 알 수 있다!
        pass









