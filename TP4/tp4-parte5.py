#interpolacion

#B = spline ((mj,Bj), K)

#K = (0, N-1, 1/fs)  -> grilla deseada

import warnings
warnings.filterwarnings('ignore')
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio

def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

mpl.rcParams['figure.figsize'] = (5,4)

sio.whosmat('ECG_TP4.mat')
mat_struct = sio.loadmat('ECG_TP4.mat')

señal = mat_struct['ecg_lead']
señal = señal.flatten(1)
N = len(señal)

fs = 1000 # Hz
nyq_frec = fs / 2


LimitInfA = int(12*60*fs)
LimitSupA = int(12.4*60*fs)

LimitInfB = int(15*60*fs)
LimitSupB = int(15.2*60*fs)

LimitInfC = int(5*60*fs)
LimitSupC = int(5.2*60*fs)

LimitInfD = int(4000)
LimitSupD = int(5500)

LimitInfE = int(10000)
LimitSupE = int(11000)


Ventana1 = sig.medfilt(señal, 201)

Ventana2 = sig.medfilt(Ventana1, 601)

X = señal - Ventana2

plt.figure(1)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfA:LimitSupA],label='ECG')
plt.plot(Ventana2[LimitInfA:LimitSupA],label='Estimación')
plt.plot(X[LimitInfA:LimitSupA],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(2)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfB:LimitSupB],label='ECG')
plt.plot(Ventana2[LimitInfB:LimitSupB],label='Estimación')
plt.plot(X[LimitInfB:LimitSupB],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(3)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfC:LimitSupC],label='ECG')
plt.plot(Ventana2[LimitInfC:LimitSupC],label='Estimación')
plt.plot(X[LimitInfC:LimitSupC],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(4)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfD:LimitSupD],label='ECG')
plt.plot(Ventana2[LimitInfD:LimitSupD],label='Estimación')
plt.plot(X[LimitInfD:LimitSupD],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(5)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfE:LimitSupE],label='ECG')
plt.plot(Ventana2[LimitInfE:LimitSupE],label='Estimación')
plt.plot(X[LimitInfE:LimitSupE],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()











