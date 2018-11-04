import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import scipy.signal as sig
import warnings
warnings.filterwarnings('ignore')

def Bartlett (N,x):
    
    ventana = sig.bartlett(N)
    
    salida = np.multiply(x,ventana)

    return salida

def normalize(d):
    # d is a (n x dimension) np array
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d


N = 1000
fs = 1000
a0 = 1

tt = np.linspace (0,((N-1)*(1/fs)),N)


L3 = 1000
K3 = 200
S = 4
R = int(L3/S)
acumuladoC = np.zeros((R))

bartlett2 = Bartlett(L3,1)
U = sum(bartlett2**2)/L3

for j in range(K3):
    for m in range(S):
        ruido = np.random.normal(0,2,N)
        fr = np.random.uniform(-0.5, 0.5, 1)
        O0 = 2*np.pi*(fs/4)
        O1 = O0 + fr*2*np.pi
        señal = a0*np.sin(O1*tt) + ruido
        bartlett1 = Bartlett(L3/S,señal[R*m:R*m+R])
        actualC = np.absolute((np.fft.fft(bartlett1))**2)
        acumuladoC += actualC
        
        
        
señal3 = acumuladoC/(K3*U*L3)
variance3 = np.var(señal3)
bias3 = np.mean(señal3/(2*np.pi*L3*U))

argmax = max(señal3)

psds = 10*np.log10(np.transpose(np.vstack([normalize(señal3)])))

plt.plot(psds)
plt.xlabel('frec. [Hz]')
plt.ylabel('PSD [W/Hz]')
plt.grid(which='both', axis='both')
plt.ylim([-50, 10])













