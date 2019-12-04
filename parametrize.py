import numpy as np


class Dot:
    def __init__(self):
        self.state = np.zeros(shape=(2, 3), dtype=np.float128)

    @property
    def x(self):
        return self.state[0][0]

    @x.setter
    def x(self, value):
        self.state[0][0] = value

    @property
    def y(self):
        return self.state[0][1]

    @y.setter
    def y(self, value):
        self.state[0][1] = value

    def __str__(self):
        return ";".join([f"{key}: {value}" for key, value in {"x": self.x, "y": self.y}.items()])

if __name__ == "__main__":
    dot = Dot()
    print(dot)
