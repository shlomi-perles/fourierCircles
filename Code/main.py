from data import Data
from dft import DFT
from exponentSeries import ExponentSeries
from visualizer import Visualizer
from pillowWriter import LoopingPillowWriter
import os


CIRCLES_NUM = int(input("How many circles?"))
IMAGE_DIRECTOR = f'D:\\'
GIFS_DIR = f'D:\\'
GIF_FPS = 50
order = CIRCLES_NUM // 2

for image in os.listdir(IMAGE_DIRECTOR):
    IMAGE_DIR = os.path.join(IMAGE_DIRECTOR, image)
    GIF_DIR = GIFS_DIR + "\\" + os.path.splitext(image)[0] + ".gif"
    imageData = Data(IMAGE_DIR)
    imageData.center()
    imageData.dataFigure()

    expSeries = ExponentSeries(imageData, order)
    DFT(imageData, expSeries)

    # imageData.plotData()
    # imageData.plotDFT()
    # imageData.plotDifferenceDFT()

    visual = Visualizer(imageData.getXTableDFT(),
                        imageData.getYTableDFT(),
                        expSeries.getExpCoef(), order,
                        imageData.getGrid(),
                        imageData.getFigLim())

    anim = visual.visualize()
    # visual.plotAnimation()
    anim.save(GIF_DIR, writer=LoopingPillowWriter(fps=GIF_FPS))
