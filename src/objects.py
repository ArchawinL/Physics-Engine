import dearpygui.dearpygui as dpg


class Object:

    def __init__(self, tag, position=(0, 0)):
        self.tag = tag
        self.x = position[0]
        self.y = position[1]


class Particle(Object):
    def __init__(self, mass, tag, position=(0, 0), velocity=(0, 0), acceleration=(0, 0)):
        super().__init__(tag, position)
        self.mass = mass
        self.velocity = velocity

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_x_velocity(self):
        return self.velocity[0]

    def get_y_velocity(self):
        return self.velocity[1]

    def draw(self):
        dpg.draw_circle(center=(self.x, self.y), radius=20, color=(255, 0, 0))
