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

tt = np.linspace (0,((N-1)*(1/fs)),N)

fr = np.random.uniform(-2, 2, 200)

O0 = np.pi /2
O1 = O0 + fr *2*np.pi /N

a = np.array([O1])

b = np.array([tt])

p = a.T * b

señal = a0*np.sin(p)

bartlett = Bartlett(N,señal)
hann     = Hann(N,señal)
blackman = Blackman(N,señal)
flattop  = Flattop(N,señal)

sp1 = np.fft.fft(bartlett)
sp2 = np.fft.fft(hann)
sp3 = np.fft.fft(blackman)
sp4 = np.fft.fft(flattop)

abs1 = np.absolute(sp1)
abs2 = np.absolute(sp2)
abs3 = np.absolute(sp3)
abs4 = np.absolute(sp4)















