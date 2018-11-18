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

