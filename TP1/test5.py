import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import statistics as stats

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes
f0 = 1

bits4 = 4
bits8 = 8
bits16 = 16

df = fs/N

tt = np.linspace (0,((N-1)*(1/fs)),N)

ff = np.linspace(0, (N-1)*df, N)

ruido = np.random.rand(N)

signal4 = (2**(bits4-1))*a0*np.sin(2*np.pi*f0*tt+p0)

signal8 = (2**(bits8-1))*a0*np.sin(2*np.pi*f0*tt+p0)

signal16 = (2**(bits16-1))*a0*np.sin(2*np.pi*f0*tt+p0)


señal4 = signal4 + ruido
señal8 = signal8 + ruido
señal16 = signal16 + ruido


grillado4 = np.around(señal4)
error4 = grillado4 - señal4

grillado8 = np.around(señal8)
error8 = grillado8 - señal8

grillado16 = np.around(señal16)
error16 = grillado16 - señal16


#plt.plot(señal1)
#plt.show()


#plt.plot(error1)
#plt.show()

#plt.hist(error1)
#plt.show()



cuadradoA1 = signal4**2
cuadradoA2 = grillado4**2
cuadradoA3 = error4**2

cuadradoB1 = signal8**2
cuadradoB2 = grillado8**2
cuadradoB3 = error8**2

cuadradoC1 = signal16**2
cuadradoC2 = grillado16**2
cuadradoC3 = error16**2

energiaA1 = integrate.simps(cuadradoA1)
energiaA2 = integrate.simps(cuadradoA2)
energiaA3 = integrate.simps(cuadradoA3)

energiaB1 = integrate.simps(cuadradoB1)
energiaB2 = integrate.simps(cuadradoB2)
energiaB3 = integrate.simps(cuadradoB3)

energiaC1 = integrate.simps(cuadradoC1)
energiaC2 = integrate.simps(cuadradoC2)
energiaC3 = integrate.simps(cuadradoC3)



sp1 = np.fft.fft(error4)
sp2 = np.fft.fft(error8)
sp3 = np.fft.fft(error16)

#plt.plot(np.absolute(sp1)[0:500])
#plt.show()
#plt.plot(np.angle(sp)[0:500])
#plt.show()

#plt.plot(20*np.log10(np.absolute(sp1)[0:500]))
#plt.show()

#regular el ruido con la varianza (o^2)sigma
Vm4  = stats.median(error4)
Vm8  = stats.median(error8)
Vm16 = stats.median(error16)

De4  = stats.pstdev(error4)
De8  = stats.pstdev(error8)
De16 = stats.pstdev(error16)

Va4  = stats.variance(error4)
Va8  = stats.variance(error8)
Va16 = stats.variance(error16)

rms4  = (energiaA3 / N)**(1/2)
rms8  = (energiaB3 / N)**(1/2)
rms16 = (energiaC3 / N)**(1/2)












