import numpy as np
from math import pi
import matplotlib.pyplot as plt
from pylab import array, xlim, ylim
from PIL import Image

FIG_SIZE = 5
LINS_START = 0
LINS_STOP = 2 * pi
LINS_NUM = 400
DEF_LEVELS = 200


class Data:
    """
    This class obtain all image's data
    """

    def __init__(self, path):
        self.__path = path
        self.__XTable, self.__YTable = self.dataAnalyze()
        self.__XTableDFT = None
        self.__YTableDFT = None
        self.__timeTable = np.linspace(LINS_START, LINS_STOP,
                                       len(self.__XTable))
        self.__grid = np.linspace(LINS_START, LINS_STOP, LINS_NUM)
        self.__figLim = None

    def getTimeTable(self):
        return self.__timeTable

    def getXTable(self):
        return self.__XTable

    def getYTable(self):
        return self.__YTable

    def getXTableDFT(self):
        return self.__XTableDFT

    def getYTableDFT(self):
        return self.__YTableDFT

    def getGrid(self):
        return self.__grid

    def getFigLim(self):
        return self.__figLim

    def setXTableDFT(self, XTableDFT):
        self.__XTableDFT = XTableDFT

    def setYTableDFT(self, YTableDFT):
        self.__YTableDFT = YTableDFT

    def dataAnalyze(self, level=None):
        """
        find path inside image
        :param level:
        :return:
        """
        if level is None:
            level = [DEF_LEVELS]
        fig, ax = plt.subplots(figsize=(FIG_SIZE, FIG_SIZE))
        ax.set_aspect('equal', 'datalim')

        # black white filter
        im = array(Image.open(self.__path).convert('L'))
        contour_plot = ax.contour(im, levels=level, colors='black',
                                  origin='image')  # one line make

        # Get  Path
        contour_path = contour_plot.collections[0].get_paths()[0]
        XTable, YTable = contour_path.vertices[:, 0], \
                         contour_path.vertices[:, 1]
        plt.close()
        return XTable, YTable

    def center(self):
        """
        center image data
        :return:
        """
        self.__XTable = self.__XTable - min(self.__XTable)
        self.__YTable = self.__YTable - min(self.__YTable)
        self.__XTable = self.__XTable - max(self.__XTable) / 2
        self.__YTable = self.__YTable - max(self.__YTable) / 2

    def dataFigure(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(self.__XTable, self.__YTable, 'k-')
        xmin, xmax = xlim()
        ymin, ymax = ylim()
        self.__figLim = [xmin, xmax, ymin, ymax]
        plt.close(fig)

    def plotData(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(self.__XTable, self.__YTable, 'k-')
        ax.set_aspect('equal', 'datalim')
        ax.set_title('Current data plot')
        ax.plot(self.__XTable, self.__YTable, 'k-')
        plt.show()
        plt.close(fig)

    def plotDFT(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_aspect('equal', 'datalim')
        ax.set_title('Current DFT plot')
        ax.plot(self.__XTableDFT, self.__YTableDFT, 'k-')
        plt.show()
        plt.close(fig)

    def plotDifferenceDFT(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_aspect('equal', 'datalim')
        ax.set_title(' Difference DFT plot')
        ax.plot(self.__XTableDFT, self.__YTableDFT, 'k--')
        ax.plot(self.__XTable, self.__YTable, 'r-')
        plt.show()
        plt.close(fig)
