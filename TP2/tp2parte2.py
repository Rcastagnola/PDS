import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import scipy.integrate as integrate
import statistics as stats

def normalize(d):
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d

N = 1000
fs = 1000
a2 = 10**(-40/20)

tt = np.linspace (0,((N-1)*(1/fs)),N)

O1 = 2*np.pi*(fs/4)
O2 = O1 + 10*2*np.pi

x1 = np.sin(O1*tt)

x2 = a2*np.sin(O2*tt)

x = x1 + x2


sp1 = np.fft.fft(x1)
plt.title('Espectro X1' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp1 = 20*np.log10(np.transpose(([normalize(np.absolute(sp1))])))
plt.plot(Nsp1[200:300])
plt.show()


sp2 = np.fft.fft(x2)
plt.title('Espectro X2' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp2 = 20*np.log10(np.transpose(([normalize(np.absolute(sp2))])))
plt.plot(Nsp2[200:300])
plt.show()


sp3 = np.fft.fft(x)
plt.title('Espectro X' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp3 = 20*np.log10(np.transpose(([normalize(np.absolute(sp3))])))
plt.plot(Nsp3[200:300])
plt.show()


Amplitud = [50,100,150,200,250,300,350]

Array = np.array([Amplitud])

Amp = 10**(-Array/20)

x2B = Amp.T*np.sin(O2*tt)

xB = x1 + x2B

sp4 = np.fft.fft(xB)

plt.title('Espectro Atenuado' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp4 = 20*np.log10(np.transpose(([normalize(np.absolute(sp4[5,]))])))
plt.plot(Nsp4[200:300])
plt.show()












