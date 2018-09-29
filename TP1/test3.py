import numpy as np
import matplotlib.pylab as plt

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes
f0 = 1


df = fs/N

tt = np.linspace (0,((N-1)*(1/fs)),N)

    
t1 = 0.5
t2 = 0.5

time1 = t1 / (t1+t2)

N1Time = N*time1
N1 = int(N1Time)
X1 = int(N1/2)

time2 = t2 / (t1+t2)

N2Time = N*time2
N2 = int(N2Time)
X2 = int(N2/2)
L2 = N-X2

ones = a0 * np.ones(N1)
zeros = -a0 * np.ones(N2)

signal = np.concatenate((ones, zeros), axis=None)

signal1 = signal[0:X1] *tt[0:X1] 
signal2 = signal[X1:N1]*(t1-tt)[X1:N1]

signal3 = signal[N1:L2] *tt[0:X2] 
signal4 = signal[L2:N]*(t2-tt)[X2:N2]

      
signal5 = np.concatenate((signal1, signal2, signal3, signal4), axis=None)

plt.title('Señal: senoidal' )
    
plt.xlabel('tiempo [segundos]')
    
plt.ylabel('Amplitud [V]')
        
plt.plot(tt, signal5)
plt.show()

