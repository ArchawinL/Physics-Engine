from src.graphics import Window
from src.objects import Particle
from utils import randomise_balls


def main():

    """
    ball1 = Particle(250, "ball1", (800, 450), (5, 0), (0, 0.1))
    ball2 = Particle(250, "ball2", (810, 460), (-4, 0), (0, 0.1))
    ball3 = Particle(250, "ball3", (760, 430), (-5, 0), (0, 0.1))
    ball4 = Particle(250, "ball4", (1000, 430), (7, 0), (0, 0.1))
    """

    ball_list = randomise_balls(5)
    mw = Window('Ball', 1600, 900)

    mw.render(ball_list)


if __name__ == '__main__':
    main()
