import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import scipy.integrate as integrate
import statistics as stats

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



N = 1000
fs = 1000
a2 = 10**(-40/20)

tt = np.linspace (0,((N-1)*(1/fs)),N)

Vector = [1,2,3,4,5,6,7,8,9,10]

Vect = np.array([Vector])

O1 = 2*np.pi*(fs/4) + 0.5*2*np.pi
O2 = 2*np.pi*(fs/4) + Vect*2*np.pi


x1 = np.sin(O1*tt)

x2 = a2*np.sin(O2.T*tt)

x = x1 + x2

rectangular = Rectangular(N,x)
bartlett = Bartlett(N,x)
hann     = Hann(N,x)
blackman = Blackman(N,x)
flattop  = Flattop(N,x)

sp0 = np.fft.fft(rectangular)
sp1 = np.fft.fft(bartlett)
sp2 = np.fft.fft(hann)
sp3 = np.fft.fft(blackman)
sp4 = np.fft.fft(flattop)

plt.title('Ventana rectangular con -300db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp0[9,])[200:300]))
plt.show()

plt.title('Ventana bartlett con -285db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp1[4,])[200:300]))
plt.show()

plt.title('Ventana hanning con -110db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp2[3,])[200:300]))
plt.show()

plt.title('Ventana blackman con -120db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp3[1,])[200:300]))
plt.show()

plt.title('Ventana flat-top con -130db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp4[1,])[200:300]))
plt.show()

