from abc import *


class Shape(ABC):
    area = 0.0

    def get_area(self):
        return self.area

    def set_area(self, a):
        self.area = a

    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError
