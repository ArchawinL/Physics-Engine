import dearpygui.dearpygui as dpg
import numpy as np


class Object:

    def __init__(self, tag, position=np.array([0, 0])):
        self.tag = tag
        self.s = position
        self.x = position[0]
        self.y = position[1]


class Particle(Object):
    def __init__(self, mass, tag, position=np.array([0, 0]), velocity=np.array([0, 0]), acceleration=np.array([0, 0]),
                 border=(1600, 900)):
        super().__init__(tag, position)
        self.mass = mass
        self.v = velocity
        self.a = acceleration

        self.v_x = velocity[0]
        self.v_y = velocity[1]
        self.a_x = acceleration[0]
        self.a_y = acceleration[1]
        self.border = border

    def move(self, elastic=True):

        if self.s[1] > self.border[1] - 50:
            self.set_velocity(np.array([self.get_x_velocity(), -self.get_y_velocity()]))
            self.s[1] = self.border[1] - 50
        elif self.s[1] < 50:
            self.set_velocity(np.array([self.get_x_velocity(), -self.get_y_velocity()]))
            self.s[1] = 50

        if self.s[0] > self.border[0] - 50:
            self.set_velocity(np.array([-self.get_x_velocity(), self.get_y_velocity()]))
            self.s[0] = self.border[0] - 50
        elif self.s[0] < 50:
            self.set_velocity(np.array([-self.get_x_velocity(), self.get_y_velocity()]))
            self.s[0] = 50

        self.v += self.a
        self.s += self.v

    """
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.x += self.v_x
        self.y += self.v_y
    """
    def set_velocity(self, v_tr: np.array):
        self.v = v_tr

    def get_x_velocity(self):
        return self.v[0]

    def get_y_velocity(self):
        return self.v[1]

    def draw(self):
        dpg.draw_circle(center=(float(self.s[0]), float(self.s[1])), radius=20, color=(255, 255, 255), tag=self.tag)
