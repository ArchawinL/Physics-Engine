import math

import dearpygui.dearpygui as dpg
import numpy as np


class Object:

    def __init__(self, tag, position=np.array([0, 0]), r=20):
        self.tag = tag
        self.s = position
        self.r = r


class Particle(Object):
    def __init__(self, density=1, tag="Particle", position=np.array([0, 0]), velocity=np.array([0, 0]),
                 acceleration=np.array([0, 0]),
                 r=20,
                 border=(1600, 900), colour=(255, 255, 255)):
        super().__init__(tag, position, r)
        self.mass = density * 4 / 3 * math.pi * r ** 3
        self.v = velocity
        self.a = acceleration
        self.border = border
        self.colour = colour

    def move(self, elasticity=1):

        if self.s[1] > self.border[1] - 50:
            self.set_velocity(np.array([self.get_x_velocity(), -self.get_y_velocity()]) * elasticity)
            self.s[1] = self.border[1] - 50
        elif self.s[1] < 50:
            self.set_velocity(np.array([self.get_x_velocity(), -self.get_y_velocity()]) * elasticity)
            self.s[1] = 50

        if self.s[0] > self.border[0] - 50:
            self.set_velocity(np.array([-self.get_x_velocity(), self.get_y_velocity()]) * elasticity)
            self.s[0] = self.border[0] - 50
        elif self.s[0] < 50:
            self.set_velocity(np.array([-self.get_x_velocity(), self.get_y_velocity()]) * elasticity)
            self.s[0] = 50

        self.v += self.a
        self.s += self.v

    def detect_collision(self, *particles, elasticity=1):

        # Optimisation 1
        index_p = particles.index(self)
        if index_p > len(particles) // 2:
            particles = particles[(len(particles) // 2):]

        else:
            particles = particles[:(len(particles) // 2)]

        for p in particles:
            disp_v = self.s - p.s
            distance = np.linalg.norm(disp_v)
            overlap = self.r + p.r - distance

            if distance < (self.r + p.r) and self.tag != p.tag:
                n_hat = disp_v / distance
                correction = (overlap / 2) * n_hat

                self.s += correction
                p.s -= correction

                rel_v = self.v - p.v
                v_rel_n = np.dot(rel_v, n_hat)

                if v_rel_n < 0:
                    impulse = (1 + elasticity) * v_rel_n / (1 / self.mass + 1 / p.mass)
                    self.v -= (impulse / self.mass) * n_hat
                    p.v += (impulse / p.mass) * n_hat

    def gravity(self, *particles, g_const=0.01):

        for p in particles:
            if p.tag != self.tag:

                disp_v = self.s - p.s
                distance = np.linalg.norm(disp_v)

                if distance != 0:
                    disp_hat = disp_v / distance

                    f_grav = (g_const * self.mass * p.mass) / (distance ** 2)
                    v_grav = f_grav * disp_hat

                    self.a -= v_grav / self.mass
                    p.a += v_grav / p.mass

    def set_velocity(self, v_tr: np.array):
        self.v = v_tr

    def get_x_velocity(self):
        return self.v[0]

    def get_y_velocity(self):
        return self.v[1]

    def draw(self):
        dpg.draw_circle(center=(float(self.s[0]), float(self.s[1])), radius=self.r, color=self.colour, tag=self.tag,
                        fill=self.colour)
