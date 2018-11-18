import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import scipy.signal as sig
import spectrum as sp
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

frec = np.zeros(200)

for h in range(200):
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
    maximoA = max(señal3)
    countA = -1
    for x in señal3[0:125]:
        countA = 1+countA   
        if x == maximoA:       
            frec[h] = countA*4

variance3 = np.var(frec)



#################################################################
frecB = np.zeros(20)

for j in range(20):
    ruidoB = np.random.normal(0,2,N)
    frB = np.random.uniform(-0.5, 0.5, 1)
    O0B = 2*np.pi*(fs/4)
    O1B = O0B + frB*2*np.pi
    señalB = a0*np.sin(O1B*tt) + ruidoB
    pARMA = sp.parma(señalB, 8, 8, 30, NFFT=N)
    
    maximoB = max(pARMA.psd)
    countB = -1
    for x in pARMA.psd[0:500]:
        countB = 1+countB   
        if x == maximoB:       
            frecB[j] = countB

variance4 = np.var(frecB)
    

        










