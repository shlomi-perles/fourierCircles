import numpy as np

def DFT(data, expSeries):
    XDFT = []
    YDFT = []
    for t in data.getGrid():
        dtExpSeries = DFTAlgo(t, expSeries)
        XDFT.append(np.real(dtExpSeries))
        YDFT.append(np.imag(dtExpSeries))
    data.setXTableDFT(XDFT)
    data.setYTableDFT(YDFT)


def DFTAlgo(t, expSeries):
    order = expSeries.getOrder()
    expCoef = expSeries.getExpCoef()
    # linear exponent span
    expBase = np.array(
        [np.exp(-n * 1j * t) for n in range(-order, order + 1)])
    expSeries = np.sum((expCoef[:, 0] + 1j * expCoef[:, 1]) * expBase[:])
    return expSeries
