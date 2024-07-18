import numpy as np

from src import *
from src.objects import Particle
from random import randint


def randomise_balls(num):
    return [Particle(250,
                     f"ball{i}",
                     (np.array([randint(50, 1500), randint(50, 750)], float)),
                     (np.array([randint(-3, 3), randint(-3, 3)], float)),
                     np.array([0, 0], float))
            for i in range(num)]

