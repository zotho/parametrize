import numpy as np


class Dot:
    def __init__(self):
        self.state = np.zeros(shape=(3), dtype=np.float128)

        def func(param):
            output = np.zeros(shape=(2), dtype=np.float128)
            output[0] = np.cos(param)
            output[1] = np.sin(param)
            return output
        self.param_func = func

    @property
    def t(self):
        return self.state[0]

    @t.setter
    def t(self, value):
        self.state[0] = value

    @property
    def x(self):
        return self.state[1]

    @x.setter
    def x(self, value):
        self.state[1] = value

    @property
    def y(self):
        return self.state[2]

    @y.setter
    def y(self, value):
        self.state[2] = value

    def step(self, dt):
        self.state[0] += dt
        self.state[1:3] = self.param_func(self.state[0])

    def __str__(self):
        return "; ".join([
            f"{key}: {value:.2f}"
            for key, value in {
                "t": self.t,
                "x": self.x,
                "y": self.y
            }.items()
        ])

if __name__ == "__main__":
    dot = Dot()
    print(dot)
    print(dot.x)
    print(dot.y)
    dot.x = 6
    print(dot.x)
    dot.y = 12e-13
    print(dot.y)
    dot.step(np.pi/4)
    print(dot)
