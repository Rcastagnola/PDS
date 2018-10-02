import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal

def Bartlett (N,x):
    
    ventana = signal.bartlett(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Hann (N,x):
    
    ventana = signal.windows.hann(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Blackman (N,x):
    
    ventana = signal.blackman(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Flattop (N,x):
    
    ventana = signal.flattop(N)
    
    salida = np.multiply(x,ventana)

    return salida

N = 1000
fs = 1000
a0 = 2
f0 = 10

señal = 1

bartlett = Bartlett(N,señal)
hann     = Hann(N,señal)
blackman = Blackman(N,señal)
flattop  = Flattop(N,señal)

sp1 = np.fft.fft(bartlett)
sp2 = np.fft.fft(hann)
sp3 = np.fft.fft(blackman)
sp4 = np.fft.fft(flattop)

plt.title('Ventana Bartlett' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(bartlett)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp1)[0:500]))
plt.show()

plt.title('Ventana Hann' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(hann)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp2)[0:500]))
plt.show()

plt.title('Ventana Blackman' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(blackman)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp3)[0:500]))
plt.show()

plt.title('Ventana Flat-top' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(flattop)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp4)[0:500]))
plt.show()




