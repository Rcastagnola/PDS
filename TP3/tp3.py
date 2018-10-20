import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
from numpy.fft import fft 

N = 1000
fs = 1000


señal = np.random.normal(0, 2, (200,1000))

sp = np.fft.fft(señal)

dp = (np.absolute(sp))**2

asd = sum(dp)/200

Esp  = stats.median(asd)

dada = abs((fft(señal))**2)/N

variance = np.var(asd)

