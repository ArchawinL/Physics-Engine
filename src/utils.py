from src import *
from src.objects import Particle
from random import randint


def randomise_balls(num):
    return [Particle(250,
                     f"ball{i}",
                     (randint(50, 1500), randint(50, 750)),
                     (randint(-10, 10), randint(-10, 10)),
                     (0, 0.1))
            for i in range(num)]

