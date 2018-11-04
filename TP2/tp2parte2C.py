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
a2A = 10**(-70/20)
a2B = 10**(-60/20)
a2C = 10**(-50/20)

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
Nsp0 = 20*np.log10(np.transpose(([normalize(np.absolute(sp1[0,]))])))
plt.plot((Nsp0[240:270]))
plt.show()

plt.title('Grafico X para d1 = 0.01 y a2 = -70db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp0A = 20*np.log10(np.transpose(([normalize(np.absolute(spA[0,]))])))
plt.plot((Nsp0A[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.01 y a2 = -60db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp0B = 20*np.log10(np.transpose(([normalize(np.absolute(spB[0,]))])))
plt.plot((Nsp0B[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.01 y a2 = -50db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp0C = 20*np.log10(np.transpose(([normalize(np.absolute(spC[0,]))])))
plt.plot((Nsp0C[240:270]))
plt.show()

plt.title('Grafico X1 para d1 = 0.25' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp1 = 20*np.log10(np.transpose(([normalize(np.absolute(sp1[1,]))])))
plt.plot((Nsp1[240:270]))
plt.show()

plt.title('Grafico X para d1 = 0.25 y a2 = -70db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp1A = 20*np.log10(np.transpose(([normalize(np.absolute(spA[1,]))])))
plt.plot((Nsp1A[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.25 y a2 = -60db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp1B = 20*np.log10(np.transpose(([normalize(np.absolute(spB[1,]))])))
plt.plot((Nsp1B[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.25 y a2 = -50db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp1C = 20*np.log10(np.transpose(([normalize(np.absolute(spC[1,]))])))
plt.plot((Nsp1C[240:270]))
plt.show()


plt.title('Grafico X1 para d1 = 0.5' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp2 = 20*np.log10(np.transpose(([normalize(np.absolute(sp1[1,]))])))
plt.plot((Nsp2[240:270]))
plt.show()

plt.title('Grafico X para d1 = 0.5 y a2 = -70db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp2A = 20*np.log10(np.transpose(([normalize(np.absolute(spA[1,]))])))
plt.plot((Nsp2A[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.5 y a2 = -60db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp2B = 20*np.log10(np.transpose(([normalize(np.absolute(spB[1,]))])))
plt.plot((Nsp2B[240:270]))
plt.show()
plt.title('Grafico X para d1 = 0.5 y a2 = -50db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp2C = 20*np.log10(np.transpose(([normalize(np.absolute(spC[1,]))])))
plt.plot((Nsp2C[240:270]))
plt.show()

