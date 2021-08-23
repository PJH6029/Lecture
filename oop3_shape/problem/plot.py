from abc import *
from tkinter import *

class PlotObject(ABC):
    @property
    @abstractmethod
    def id(self):
        raise NotImplementedError

    @abstractmethod
    def move(self, to_x, to_y):
        raise NotImplementedError

    @abstractmethod
    def display(self, canvas):
        raise NotImplementedError


class Painter:
    def __init__(self, width=None, height=None):
        self.root = Tk()
        self.root.resizable(True, True)
        if (width is not None) and (height is not None):
            self.canvas = Canvas(self.root, width=width, height=height)
        if width is not None:
            self.canvas = Canvas(self.root, width=width)
        if height is not None:
            self.canvas = Canvas(self.root, height=height)
        else:
            self.canvas = Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

    def draw_object(self, plot_obj):
        plot_obj.display(self.canvas)

    def draw_many_objects(self, *plot_obj_list):
        for plot_obj in plot_obj_list:
            plot_obj.display(self.canvas)

    def move_object(self, *plot_objs, to_x, to_y):
        for plot_obj in plot_objs:
            plot_obj.move(to_x, to_y)
            self.canvas.move(plot_obj.id, to_x, to_y)
        self.root.update()

    def show(self):
        self.root.mainloop()
