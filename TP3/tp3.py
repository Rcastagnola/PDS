import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import scipy.signal as sig

def Bartlett (N,x):
    
    ventana = sig.bartlett(N)
    
    salida = np.multiply(x,ventana)

    return salida


N1 = [10, 50, 100, 250, 500, 1000, 5000]
variance1 = np.zeros(7)
bias1 = np.zeros(7)

for i1 in range (7):
    
    señalA = np.random.normal(0, 2, (N1[i1]))
    Estimador = np.absolute((np.fft.fft(señalA))**2)/N1[i1]
    variance1[i1] = np.var(Estimador)
    bias1[i1] = np.mean(Estimador/(2*np.pi))

###########################################################
K2 = 10
L2 = [10, 50, 100, 250, 500, 1000, 5000]

variance2 = np.zeros(7)
bias2 = np.zeros(7)

for i2 in range (7):
    
    acumuladoB = np.zeros((L2[i2]))

    for j in range(K2):
    
        señalB = np.random.normal(0,2,(L2[i2]))
        actualB = np.absolute((np.fft.fft(señalB))**2)/L2[i2]
        acumuladoB += actualB
        señal2 = acumuladoB/K2
        variance2[i2] = np.var(señal2)
        bias2[i2] = np.mean(señal2/(2*np.pi))

#############################################################
L3 = [10, 50, 100, 250, 500, 1000, 5000]
K3 = 10
S = 2

variance3 = np.zeros(7)
bias3 = np.zeros(7)

for i3 in range (7):

    R = int(L3[i3]/S)
    acumuladoC = np.zeros((R))

    bartlett2 = Bartlett(L3[i3],1)
    U = sum(bartlett2**2)/L3[i3]

    for j in range(K3):
        for m in range(S):
            señalC = np.random.normal(0,2,(L3[i3]))
            bartlett1 = Bartlett(L3[i3]/S,señalC[R*m:R*m+R])
            actualC = np.absolute((np.fft.fft(bartlett1))**2)
            acumuladoC += actualC
            señal3 = acumuladoC/(K3*U*L3[i3])
            variance3[i3] = np.var(señal3)
            bias3[i3] = np.mean(señal3/(2*np.pi*L3[i3]*U))

        
            

