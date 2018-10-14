import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import scipy.integrate as integrate
import statistics as stats


N = 1000
fs = 1000
a2 = 10**(-40/20)


tt = np.linspace (0,((N-1)*(1/fs)),N)

O1 = np.pi /2
O2 = O1 + 10 *2*np.pi /N

x1 = np.sin(O1*tt)

x2 = a2*np.sin(O2*tt)

x = x1 + x2

sp1 = np.fft.fft(x1)
plt.title('Espectro X1' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp1)[0:50]))
plt.show()


sp2 = np.fft.fft(x2)
plt.title('Espectro X2' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp2)[0:50]))
plt.show()


sp3 = np.fft.fft(x)
plt.title('Espectro X' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp3)[0:50]))
plt.show()

grillado = np.around(x)
error = grillado - x

plt.hist(error)
plt.show()

maximoX1 = max(20*np.log10(np.absolute(sp1)[0:50]))

maximoX2 = max(20*np.log10(np.absolute(sp2)[0:50]))

maximoX = max(20*np.log10(np.absolute(sp3)[0:50]))


