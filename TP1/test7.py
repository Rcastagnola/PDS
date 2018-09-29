import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate


def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """ 
    
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """    

    # comienzo de la función

    tt = np.linspace (0,((N-1)*(1/fs)),N)

    signal = a0*np.sin(2*np.pi*f0*tt+p0)
    
    plt.title('Señal: senoidal' )
    plt.xlabel('tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    
    plt.plot(tt, signal)

    plt.show()
    
    # fin de la función
    
    return tt, signal

N  = 1000 # muestras
fs = 1000 # Hz
a0 = 1 # Volts
p0 = 0 # radianes
f0 = 10   # Hz

tt, signal = generador_senoidal (fs, f0, N, a0, p0)


zeros = np.zeros((N), dtype=np.complex)

for k in range(N):
    
    for n in range(N):
        
        zeros[k] = zeros[k] + signal[n] * np.exp(-1j*2*np.pi*k*n/N)
        
plt.title('DFT MANUAL' )
plt.xlabel('frecuencia [Hz]')
plt.ylabel('Amplitud')        
plt.stem(np.absolute(zeros)[0:500])
plt.show()

plt.title('DFT por función' )
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
sp = np.fft.fft(signal)
plt.stem(np.absolute(sp)[0:500])
plt.show()













        