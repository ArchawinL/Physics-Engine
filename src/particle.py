class Particle:
    def __init__(self, mass, position=(0, 0), velocity=(0, 0)):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def move(self):
        self.position = tuple(map(sum, zip(self.position, self.velocity)))

    def set_velocity(self, velocity):
        self.velocity = velocity


