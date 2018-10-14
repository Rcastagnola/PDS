import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import scipy.integrate as integrate
import statistics as stats


N = 1000
fs = 1000
a2 = 10**(-40/20)

tt = np.linspace (0,((N-1)*(1/fs)),N)

d1 = [0.01,0.25,0.5] 

a = np.array([d1])

O1 = np.pi /2 + a*2*np.pi /N
O2 = O1 + 10 *2*np.pi /N

x1 = np.sin(O1.T*tt)

x2 = a2*np.sin(O2.T*tt)

x = x1 + x2

sp2 = np.fft.fft(x2)

abso = np.absolute(sp2)

plt.title('d1 = 0.01' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp2[0,])[0:10])
plt.show()

plt.title('d1 = 0.25' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp2[1,])[0:10])
plt.show()


plt.title('d1 = 0.5' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp2[2,])[0:10])
plt.show()

