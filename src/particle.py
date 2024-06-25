class Particle:
    def __init__(self, mass, position=(0, 0), velocity=(0, 0)):
        self.mass = mass
        self.x = position[0]
        self.y = position[1]
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



