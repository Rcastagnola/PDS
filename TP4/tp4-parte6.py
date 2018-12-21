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

hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])

latidos = mat_struct['qrs_detections']
latidos = latidos.flatten(1)


distancia = np.zeros(1902)
latidosB = np.zeros(1903)

for o in range (1902):
    distancia[o] = latidos[o+1] - latidos[o]
    
titi = max(distancia)
toto = min(distancia)
    

Ventana1 = sig.medfilt(señal, 201)

Ventana2 = sig.medfilt(Ventana1, 601)

X = señal - Ventana2


z=500
i=0
for y in range (N):
    z = z+1
    if z > 375:
        if X[y] < (-2000):
            latidosB[i] = y
            i = i+1
            z = 0
            
        
resta = latidosB - latidos

tt = np.linspace (0,1899,1900)

plt.plot(tt,resta[0:1900])

