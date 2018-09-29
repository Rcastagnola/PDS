import numpy as np
import matplotlib.pylab as plt

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes
f0 = 1

df = fs/N


t1 = 0.4
t2 = 0.6

time1 = t1 / (t1+t2)

N1Time = N*time1
N1 = int(N1Time)

time2 = t2 / (t1+t2)

N2Time = N*time2
N2 = int(N2Time)

ones = a0 * np.ones(N1)
zeros = a0 * np.zeros(N2)

signal = np.concatenate((ones, zeros), axis=None)

        
plt.title('Señal: senoidal' )
    
plt.xlabel('tiempo [segundos]')
    
plt.ylabel('Amplitud [V]')
        
plt.plot(signal)
plt.show()

#plt.hist(signal)