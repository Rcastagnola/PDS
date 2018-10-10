import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal
import statistics as stats

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

sp1 = np.fft.fft(bartlett)*O0
sp2 = np.fft.fft(hann)*O0
sp3 = np.fft.fft(blackman)*O0
sp4 = np.fft.fft(flattop)*O0

abs1 = np.absolute(sp1)
abs2 = np.absolute(sp2)
abs3 = np.absolute(sp3)
abs4 = np.absolute(sp4)


Est1 = abs1.T[1,]
Est2 = abs2.T[1,]
Est3 = abs3.T[1,]
Est4 = abs4.T[1,]

Esp1  = stats.median(Est1)
Esp2  = stats.median(Est2)
Esp3  = stats.median(Est3)
Esp4  = stats.median(Est4)

Sesgo1 = Esp1 - a0
Var1  = stats.variance(Est1)

Sesgo2 = Esp2 - a0
Var2  = stats.variance(Est2)

Sesgo3 = Esp3 - a0
Var3  = stats.variance(Est3)

Sesgo4 = Esp4 - a0
Var4  = stats.variance(Est4)

plt.title('Histograma Bartlett' )
plt.hist(Est1)
plt.show()
plt.title('Histograma Hann' )
plt.hist(Est2)
plt.show()
plt.title('Histograma Blackman' )
plt.hist(Est3)
plt.show()
plt.title('Histograma Flat-top' )
plt.hist(Est4)
plt.show()

