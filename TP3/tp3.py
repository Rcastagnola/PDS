import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import statistics as stats

N = 1000
fs = 1000


señal = np.random.normal(0, 2, (200,1000))

sp = np.fft.fft(señal)

dp = (np.absolute(sp))**2

asd = sum(dp)/200

Var  = stats.variance(asd)

Esp  = stats.median(asd)
