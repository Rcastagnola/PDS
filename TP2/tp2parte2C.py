import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import scipy.integrate as integrate
import statistics as stats


N = 1000
fs = 1000
a2A = 10**(-35/20)
a2B = 10**(-30/20)
a2C = 10**(-25/20)

tt = np.linspace (0,((N-1)*(1/fs)),N)

d1 = [0.01,0.25,0.5] 

a = np.array([d1])

O1 = 2*np.pi*(fs/4) + a*2*np.pi
O2 = O1 + 10 *2*np.pi

x1 = np.sin(O1.T*tt)

x2A = a2A*np.sin(O2.T*tt)
x2B = a2B*np.sin(O2.T*tt)
x2C = a2C*np.sin(O2.T*tt)

xA = x1 + x2A
xB = x1 + x2B
xC = x1 + x2C

spA = np.fft.fft(xA)
spB = np.fft.fft(xB)
spC = np.fft.fft(xC)

sp1 = np.fft.fft(x1) 

plt.title('Grafico X1 para d1 = 0.01' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp1[0,])[240:270])
plt.show()

plt.title('Grafico X para d1 = 0.01 y a2 = -35db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spA[0,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.01 y a2 = -30db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spB[0,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.01 y a2 = -25db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spC[0,])[240:270])
plt.show()

plt.title('Grafico X1 para d1 = 0.25' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp1[1,])[240:270])
plt.show()

plt.title('Grafico X para d1 = 0.25 y a2 = -35db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spA[1,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.25 y a2 = -30db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spB[1,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.25 y a2 = -25db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spC[1,])[240:270])
plt.show()


plt.title('Grafico X1 para d1 = 0.5' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(sp1[2,])[240:270])
plt.show()

plt.title('Grafico X para d1 = 0.5 y a2 = -35db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spA[2,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.5 y a2 = -30db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spB[2,])[240:270])
plt.show()
plt.title('Grafico X para d1 = 0.5 y a2 = -25db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
plt.stem(np.absolute(spC[2,])[240:270])
plt.show()

