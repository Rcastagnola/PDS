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


#hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
#hb_2 = vertical_flaten(mat_struct['heartbeat_pattern2'])

#plt.figure(1)
#plt.plot(señal[0:12000])
#sp = np.fft.fft(señal[0:10000])
#plt.figure(2)
#plt.plot(np.absolute(sp[0:100]))


######################################################################
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 2.0 #Hz
wp2 = 40.0 #Hz
ws2 = 45.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)

#######################################################################
cant_coef = 501

FiltroWin = sig.firwin2(cant_coef, frecs, gains , window='hamming' )

_, spWin = sig.freqz(FiltroWin)

señalWin = sig.filtfilt(FiltroWin,1, señal)
#######################################################################
FiltroRemez = sig.remez(501, [0, 0.001, 0.002, 0.04, 0.045,0.5], [0, 1, 0])

_, spRemez = sig.freqz(FiltroRemez)

señalRemez = sig.filtfilt(FiltroRemez,1, señal)

########################################################################
FiltroButter = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype='butter', output='sos')

_, spButter = sig.sosfreqz(FiltroButter)

señalButter = sig.sosfiltfilt(FiltroButter, señal)

###########################################################################
FiltroCheby = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype='cheby2', output='sos')

_, spCheby = sig.sosfreqz(FiltroCheby)

señalCheby = sig.sosfiltfilt(FiltroCheby, señal)

########################################################################
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

plt.figure(1)
plt.title('Respuesta de los filtros')
plt.plot(20 * np.log10(abs(spWin[0:100])),label='Hamming')
plt.plot(20 * np.log10(abs(spButter[0:100])),label='Butter')
plt.plot(20 * np.log10(abs(spRemez[0:100])),label='Remez')
plt.plot(20 * np.log10(abs(spCheby[0:100])),label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(2)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfA:LimitSupA],label='ECG')
plt.plot(señalWin[LimitInfA:LimitSupA],label='Hamming')
plt.plot(señalButter[LimitInfA:LimitSupA],label='Butter')
plt.plot(señalRemez[LimitInfA:LimitSupA],label='Remez')
plt.plot(señalCheby[LimitInfA:LimitSupA],label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(3)
plt.title('Zona con interferencia')
plt.plot(señal[LimitInfB:LimitSupB],label='ECG')
plt.plot(señalWin[LimitInfB:LimitSupB],label='Hamming')
plt.plot(señalButter[LimitInfB:LimitSupB],label='Butter')
plt.plot(señalRemez[LimitInfB:LimitSupB],label='Remez')
plt.plot(señalCheby[LimitInfB:LimitSupB],label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(4)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfC:LimitSupC],label='ECG')
plt.plot(señalWin[LimitInfC:LimitSupC],label='Hamming')
plt.plot(señalButter[LimitInfC:LimitSupC],label='Butter')
plt.plot(señalRemez[LimitInfC:LimitSupC],label='Remez')
plt.plot(señalCheby[LimitInfC:LimitSupC],label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(5)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfD:LimitSupD],label='ECG')
plt.plot(señalWin[LimitInfD:LimitSupD],label='Hamming')
plt.plot(señalButter[LimitInfD:LimitSupD],label='Butter')
plt.plot(señalRemez[LimitInfD:LimitSupD],label='Remez')
plt.plot(señalCheby[LimitInfD:LimitSupD],label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(6)
plt.title('Zona sin interferencia')
plt.plot(señal[LimitInfE:LimitSupE],label='ECG')
plt.plot(señalWin[LimitInfE:LimitSupE],label='Hamming')
plt.plot(señalButter[LimitInfE:LimitSupE],label='Butter')
plt.plot(señalRemez[LimitInfE:LimitSupE],label='Remez')
plt.plot(señalCheby[LimitInfE:LimitSupE],label='Cheby')

axes_hdl = plt.gca()
axes_hdl.legend()



