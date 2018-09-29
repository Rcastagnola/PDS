import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes

f0 = int(9)


df = fs/N

tt = np.linspace (0,((N-1)*(1/fs)),N)

ff = np.linspace(0, (N-1)*df, N)
    
signal = a0*np.sin(2*np.pi*f0*tt+p0)


N1 = int(N/10)
N2 = int(N*10)

Ceros1 = np.zeros(N1)

Ceros2 = np.zeros(N2)


resultado = np.concatenate((Ceros1, signal , Ceros2), axis=None)

plt.plot(resultado)
plt.show()

sp = np.fft.fft(resultado)


plt.stem(np.absolute(sp)[0:500])
plt.show()
#plt.plot(np.angle(sp)[0:500])

#plt.show()


cuadrado = (np.absolute(sp)[0:500])**2
energia = integrate.simps(cuadrado)

cuadrado0 = (np.absolute(sp)[f0])**2

plt.plot(20*np.log10(np.absolute(sp)[0:500]))
plt.show()


asd = max(cuadrado)


count = -1
for x in cuadrado:
    count = 1+count   
    if x == asd:       
        frec = count
        
        
        
        