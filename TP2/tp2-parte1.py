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

i = -1
j = -1

c = np.zeros((200, 1000))

for x in O1:
    i = i+1    
    for y in tt:
        j = j+1
        c[i,j] = x*y





#asd = a0*np.sin(2*np.pi*f0*tt)

#wind = signal.hamming(N)

#hamming = np.multiply(asd,wind)

#plt.plot(hamming)
#plt.show()

#sp = np.fft.fft(hamming)

#plt.plot(np.absolute(sp)[0:500])
#plt.show()



