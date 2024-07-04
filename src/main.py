from src.graphics import Window
from src.objects import Particle


def main():

    ball1 = Particle(250, "ball1", (800, 450), (5, 0), (0, 0.1))
    ball2 = Particle(250, "ball2", (810, 460), (-4, 0), (0, 0.1))
    ball3 = Particle(250, "ball3", (760, 430), (-5, 0), (0, 0.1))
    ball4 = Particle(250, "ball4", (1000, 430), (7, 0), (0, 0.1))


    mw = Window('Custom Title', 1600, 900)

    mw.render([ball1, ball2, ball3, ball4])


if __name__ == '__main__':
    main()
