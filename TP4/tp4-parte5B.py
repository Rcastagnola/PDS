import warnings
warnings.filterwarnings('ignore')
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.interpolate as inte

def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

mpl.rcParams['figure.figsize'] = (5,4)

sio.whosmat('ECG_TP4.mat')
mat_struct = sio.loadmat('ECG_TP4.mat')

señal = mat_struct['ecg_lead']
señal = señal.flatten(1)

sio.whosmat('ECG_TP4.mat')
loc_lat = sio.loadmat('ECG_TP4.mat')

latidos = loc_lat['qrs_detections']
latidos = latidos.flatten(1)

N = len(señal)

fs = 1000 # Hz
nyq_frec = fs / 2


latidos_50 = latidos - 50

vector = señal[latidos_50]

asd = inte.CubicSpline(latidos_50,vector)

estimacion = np.zeros(N)

for x in range(N):
    estimacion[x] = asd(x)
    

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

X2 = señal - estimacion

plt.figure(1)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfA:LimitSupA],label='ECG')
plt.plot(estimacion[LimitInfA:LimitSupA],label='Estimación')
plt.plot(X2[LimitInfA:LimitSupA],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(2)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfB:LimitSupB],label='ECG')
plt.plot(estimacion[LimitInfB:LimitSupB],label='Estimación')
plt.plot(X2[LimitInfB:LimitSupB],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(3)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfC:LimitSupC],label='ECG')
plt.plot(estimacion[LimitInfC:LimitSupC],label='Estimación')
plt.plot(X2[LimitInfC:LimitSupC],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(4)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfD:LimitSupD],label='ECG')
plt.plot(estimacion[LimitInfD:LimitSupD],label='Estimación')
plt.plot(X2[LimitInfD:LimitSupD],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(5)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfE:LimitSupE],label='ECG')
plt.plot(estimacion[LimitInfE:LimitSupE],label='Estimación')
plt.plot(X2[LimitInfE:LimitSupE],label='Corrección')

axes_hdl = plt.gca()
axes_hdl.legend()





















