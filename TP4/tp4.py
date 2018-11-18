## Inicialización del Notebook del TP4

import numpy as np
from pandas import DataFrame
from IPython.display import HTML
from scipy import signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt




def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

ww, hh = sig.freqz(np.array([1,0,0,0, -1]), [1])
ww = ww / np.pi

plt.figure(1)

plt.plot(ww,(abs(hh)), label='ejemplo')
#plt.plot(ww, 20 * np.log10(abs(hh)), label='ejemplo')

plt.title('FIR ejemplo')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.show()