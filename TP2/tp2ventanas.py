import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import warnings
warnings.filterwarnings('ignore')

def Rectangular (N,x):
    
    ventana = signal.boxcar(N)
    
    salida = np.multiply(x,ventana)

    return salida

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

def normalize(d):
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d

N = 1000
fs = 1000
a0 = 2
f0 = 10

señal = 1

rectangular = Rectangular(N,señal)
bartlett = Bartlett(N,señal)
hann     = Hann(N,señal)
blackman = Blackman(N,señal)
flattop  = Flattop(N,señal)

sp0 = np.fft.fft(rectangular,4096)/25.5
sp1 = np.fft.fft(bartlett,4096)/25.5
sp2 = np.fft.fft(hann,4096)/25.5
sp3 = np.fft.fft(blackman,4096)/25.5
sp4 = np.fft.fft(flattop,4096)/25.5

freq = np.linspace(0, 1, 100)

plt.title('Ventana Rectangular' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(rectangular)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
Nsp0 = 20*np.log10(np.transpose(([normalize(np.absolute(sp0))])))
plt.plot(freq, Nsp0[0:100])
plt.show()

plt.title('Ventana Bartlett' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(bartlett)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
Nsp1 = 20*np.log10(np.transpose(([normalize(np.absolute(sp1))])))
plt.plot(freq, Nsp1[0:100])
plt.show()

plt.title('Ventana Hann' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(hann)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
Nsp2 = 20*np.log10(np.transpose(([normalize(np.absolute(sp2))])))
plt.plot(freq, Nsp2[0:100])
plt.show()

plt.title('Ventana Blackman' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(blackman)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
Nsp3 = 20*np.log10(np.transpose(([normalize(np.absolute(sp3))])))
plt.plot(freq, Nsp3[0:100])
plt.show()

plt.title('Ventana Flat-top' )
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.plot(flattop)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
Nsp4 = 20*np.log10(np.transpose(([normalize(np.absolute(sp4))])))
plt.plot(freq, Nsp4[0:100])
plt.show()

maxi0 = max(Nsp0[4:2048])
maxi1 = max(Nsp1[8:2048])
maxi2 = max(Nsp2[8:2048])
maxi3 = max(Nsp3[12:2048])
maxi4 = np.round(max(Nsp4[22:2048]),2)



