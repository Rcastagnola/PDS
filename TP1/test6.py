import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate


N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes

f0 = int(9*fs/N)

df = fs/N

tt = np.linspace (0,((N-1)*(1/fs)),N)

ff = np.linspace(0, (N-1)*df, N)

signal = a0*np.sin(2*np.pi*f0*tt+p0)
signal1 = a0*np.sin(2*np.pi*f0*tt+np.pi)

zeros = a0 * np.zeros(N)

resultado = np.concatenate((signal[0:111], signal1[111:222], zeros[222:1000]), axis=None)

plt.plot(tt, signal)
plt.show()

sp = np.fft.fft(resultado)

#plt.stem(np.absolute(sp)[0:500])
#plt.show()


#sp1 = np.fft.fft(resultado)

#plt.stem(np.absolute(sp1)[0:500])
#plt.show()


#plt.plot(20*np.log10(np.absolute(sp1)[0:500]))
#plt.show()

cuadrado = (np.absolute(sp)[0:500])**2
energia = integrate.simps(cuadrado)

#cuadrado0 = (np.absolute(sp)[f0])**2

asd = max(cuadrado)


count = -1
for x in cuadrado:
    count = 1+count   
    if x == asd:       
        frec = count
        
        
        
        
        
        
        
        
        
        
