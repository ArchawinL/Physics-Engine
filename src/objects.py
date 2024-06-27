import dearpygui.dearpygui as dpg
import numpy as np


class Object:

    def __init__(self, tag, position=(0, 0)):
        self.tag = tag
        self.x = position[0]
        self.y = position[1]


class Particle(Object):
    def __init__(self, mass, tag, position=(0, 0), velocity=(0, 0), acceleration=(0, 0)):
        super().__init__(tag, position)
        self.mass = mass
        self.v_x = velocity[0]
        self.v_y = velocity[1]
        self.a_x = acceleration[0]
        self.a_y = acceleration[1]

    def move(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.x += self.v_x
        self.y += self.v_y

    def set_velocity(self, velocity):
        self.v_x = velocity[0]
        self.v_y = velocity[1]

    def get_x_velocity(self):
        return self.v_x

    def get_y_velocity(self):
        return self.v_y

    def draw(self):
        dpg.draw_circle(center=(self.x, self.y), radius=20, color=(255, 255, 255), tag=self.tag)
