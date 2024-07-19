import dearpygui.dearpygui as dpg
import numpy as np


class Object:

    def __init__(self, tag, position=np.array([0, 0]), r=20):
        self.tag = tag
        self.s = position
        self.x = position[0]
        self.y = position[1]
        self.r = r


class Particle(Object):
    def __init__(self, mass, tag, position=np.array([0, 0]), velocity=np.array([0, 0]), acceleration=np.array([0, 0]),
                 r=50,
                 border=(1600, 900)):
        super().__init__(tag, position, r)
        self.mass = mass
        self.v = velocity
        self.a = acceleration
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

    def detect_collision(self, *particles):
        for p in particles:
            disp_v = self.s - p.s

            if np.linalg.norm(disp_v) < self.r * 2 and self.tag != p.tag:
                self.s += np.divide(disp_v, 2)
                p.s -= np.divide(disp_v, 2)
                disp_v = self.s - p.s

                """Tangential Velocities calculation"""
                n_hat = np.divide(disp_v, np.linalg.norm(disp_v))
                t_hat = np.array([-n_hat[1], n_hat[0]], float)

                v_1tp = np.multiply(t_hat, np.dot(t_hat, self.v))
                v_2tp = np.multiply(t_hat, np.dot(t_hat, p.v))

                """Normal Velocities calculation"""
                v_1n = np.dot(n_hat, self.v)
                v_2n = np.dot(n_hat, p.v)
                """
                self.set_velocity(v_1tp)
                p.set_velocity(v_2tp)
                """

    def set_velocity(self, v_tr: np.array):
        self.v = v_tr

    def get_x_velocity(self):
        return self.v[0]

    def get_y_velocity(self):
        return self.v[1]

    def draw(self):
        dpg.draw_circle(center=(float(self.s[0]), float(self.s[1])), radius=self.r, color=(255, 255, 255), tag=self.tag,
                        fill=(255, 255, 255))
