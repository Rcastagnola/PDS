import numpy as np
import matplotlib.pylab as plt

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes

fd1 = 0.01
fd2 = 0.25
fd3 = 0.5

f0 = fs/4
f01 = fs/4 + fd1
f02 = fs/4 + fd2
f03 = fs/4 + fd3

df = fs/N


tt = np.linspace (0,((N-1)*(1/fs)),N)

ff = np.linspace(0, (N-1)*df, N)

signal0 = a0*np.sin(2*np.pi*f0*tt+p0)    
signal1 = a0*np.sin(2*np.pi*f01*tt+p0)
signal2 = a0*np.sin(2*np.pi*f02*tt+p0)
signal3 = a0*np.sin(2*np.pi*f03*tt+p0)

sp0 = np.fft.fft(signal0)

sp1 = np.fft.fft(signal1)

plt.stem(np.absolute(sp1)[0:500])
plt.show()


sp2 = np.fft.fft(signal2)

plt.stem(np.absolute(sp2)[0:500])
plt.show()


sp3 = np.fft.fft(signal3)

plt.stem(np.absolute(sp3)[0:500])
plt.show()


x01 = np.absolute(sp0)[250]
x11 = np.absolute(sp1)[250]
x21 = np.absolute(sp2)[250]
x31 = np.absolute(sp3)[250]

x02 = np.absolute(sp0)[251]
x12 = np.absolute(sp1)[251]
x22 = np.absolute(sp2)[251]
x32 = np.absolute(sp3)[251]

x03 = sum(np.absolute(sp0)[0:500])-np.absolute(sp0)[250]
x13 = sum(np.absolute(sp1)[0:500])-np.absolute(sp1)[250]
x23 = sum(np.absolute(sp2)[0:500])-np.absolute(sp2)[250]
x33 = sum(np.absolute(sp3)[0:500])-np.absolute(sp3)[250]







