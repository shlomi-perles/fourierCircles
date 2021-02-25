from math import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

LINE_WIDTH = 2
RADIUS_WIDTH = 1
MARKER_SIZE = 1
CIRCLE_WIDTH = 0.5

LINE_COLOR = 'w-'
RDIUS_COLOR = 'lightgrey'
CIRCLE_COLOR = 'dimgrey'
MARKER_STYLE = 'o'

BACKGROUND = 'dark_background'


class Visualizer:
    """
    This class obtain all image's data
    """

    def __init__(self, XDFT, YDFT, coef, order, space, figLim):
        self.__XDFT = XDFT
        self.__YDFT = YDFT
        self.__coef = coef
        self.__order = order
        self.__space = space
        self.__figLim = figLim

    def visualize(self):
        plt.style.use(BACKGROUND)
        fig, ax = plt.subplots()
        lim = max(self.__figLim)
        ax.set_xlim([-lim, lim])
        ax.set_ylim([-lim, lim])
        ax.set_aspect('equal')

        # Initial objects
        self.__line = plt.plot([], [], LINE_COLOR, linewidth=LINE_WIDTH)[0]
        self.__radius = [
            plt.plot([], [], RDIUS_COLOR, linewidth=RADIUS_WIDTH,
                     marker=MARKER_STYLE, markersize=MARKER_SIZE)[0]
            for _ in range(2 * self.__order + 1)]
        self.__circles = [
            plt.plot([], [], CIRCLE_COLOR, linewidth=CIRCLE_WIDTH)[0]
            for _ in range(2 * self.__order + 1)]

        ani = animation.FuncAnimation(fig, self.animate,
                                      frames=len(self.__space), interval=5)
        return ani

    def updateCoef(self, coef, t):
        new_c = []
        for i, j in enumerate(range(-self.__order, self.__order + 1)):
            dtheta = -j * t
            ct, st = np.cos(dtheta), np.sin(dtheta)
            v = [ct * coef[i][0] - st * coef[i][1],
                 st * coef[i][0] + ct * coef[i][1]]
            new_c.append(v)
        return np.array(new_c)

    def sortVelocity(self):
        idx = []
        for i in range(1, self.__order + 1):
            idx.extend([self.__order + i, self.__order - i])
        return idx

    def animate(self, i):
        # animate lines
        self.__line.set_data(self.__XDFT[:i], self.__YDFT[:i])

        # animate circles
        r = [np.linalg.norm(self.__coef[j]) for j in
             range(len(self.__coef))]
        pos = self.__coef[self.__order]
        coefs = self.updateCoef(self.__coef, i / len(self.__space) * 2 * pi)
        idx = self.sortVelocity()

        for j, rad, circle in zip(idx, self.__radius, self.__circles):
            newPos = pos + coefs[j]
            rad.set_data([pos[0], newPos[0]], [pos[1], newPos[1]])
            theta = np.linspace(0, 2 * pi, 50)
            x, y = r[j] * np.cos(theta) + pos[0], r[j] * \
                   np.sin(theta) + pos[1]
            circle.set_data(x, y)
            pos = newPos

    def plotAnimation(self):
        plt.show()

