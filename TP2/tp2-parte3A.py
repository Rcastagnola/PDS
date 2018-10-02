import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal


N = 1000
fs = 1000
a0 = 2
f0 = 10

tt = np.linspace (0,((N-1)*(1/fs)),N)

fr = np.random.uniform(-2, 2, 200)

O0 = np.pi /2
O1 = O0 + fr *2*np.pi /N

x = a0*np.sin(O1)



c = np.zeros((200, 1000))






