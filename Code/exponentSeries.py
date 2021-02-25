from scipy.integrate import quad
import numpy as np
from math import pi

INTEGRAL_LIMIT = 150
INTEGRAL_START = 0
INTEGRAL_END = 2 * pi


class ExponentSeries:
    """
    This class obtain the exponent series coefficients
    """

    def __init__(self, data, order):
        self.__expCoef = coefList(data, order)
        self.__order = order

    def getExpCoef(self):
        return self.__expCoef

    def getOrder(self):
        return self.__order


def coefList(data, order):
    """
    numeric integral exponent
    :param data:
    :param order:
    :return:
    """
    coefLst = []
    for n in range(-order, order + 1):
        realCoef = quad(lambda t: np.real(
            linearInterpolan(t, data) * np.exp(-n * 1j * t)),
                        INTEGRAL_START, INTEGRAL_END, limit=INTEGRAL_LIMIT,
                        full_output=1)[0] / (2 * pi)
        imagCoef = quad(lambda t: np.imag(
            linearInterpolan(t, data) * np.exp(-n * 1j * t)),
                        INTEGRAL_START, INTEGRAL_END, limit=INTEGRAL_LIMIT,
                        full_output=1)[0] / (2 * pi)
        coefLst.append([realCoef, imagCoef])
    return np.array(coefLst)


def linearInterpolan(t, data):
    """
    aprox point between two points
    :param t:
    :param data:
    :return:
    """
    return np.interp(t, data.getTimeTable(), data.getXTable()) + 1j * \
           np.interp(t, data.getTimeTable(), data.getYTable())
