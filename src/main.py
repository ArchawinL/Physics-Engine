from src.graphics import Window
from src.objects import Particle


def main():
    ball = Particle(250, "ball", (800, 450), (5, 6), (0, 0))
    mw = Window('Custom Title', 1600, 900)

    mw.render([ball])


if __name__ == '__main__':
    main()
