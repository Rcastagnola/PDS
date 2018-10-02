import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

N = 256  # number of samples
M = 5  # number of sample functions

# generate random signal
np.random.seed(1)
x = np.random.normal(size=(M, N))
h = sig.firwin2(N, [0, .5, .52, .55, .57, 1], [0, 0, 1, 1, 0, 0])
x = [np.convolve(xi, h, mode='same') for xi in x]

# DFT of signal
X = np.fft.rfft(x, axis=1)
Om = np.linspace(0, np.pi, X.shape[1])

# plot signal and its spectrum
plt.figure(figsize=(10,4))
plt.plot(Om, np.abs(X.T))
plt.title('Magnitude spectrum')
plt.xlabel(r'$\Omega[\mu]$')
plt.ylabel(r'$|X[\mu]|$')
plt.axis([0, np.pi, 0, 30]);