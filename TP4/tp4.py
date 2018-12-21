## Inicialización del Notebook del TP4

import numpy as np
from pandas import DataFrame
from IPython.display import HTML
from scipy import signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt




def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

ww, hh = sig.freqz(np.array([1/3,1/3,1/3]), [1])
ww = ww / np.pi

plt.figure(1)

plt.plot(ww,(abs(hh)))

plt.title('N=3')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo')
plt.grid(which='both', axis='both')



plt.figure(2)
plt.plot(ww, 20 * np.log10(abs(hh)))

plt.title('N=3')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

plt.show()

ww2, hh2 = sig.freqz(np.array([1/3,1/3,1/3,1/3,1/3]), [1])
ww2 = ww2 / np.pi

plt.figure(3)

plt.plot(ww,(abs(hh2)))

plt.title('N=5')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo')
plt.grid(which='both', axis='both')


plt.figure(4)
plt.plot(ww2, 20 * np.log10(abs(hh2)))

plt.title('N=5')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

plt.show()

ww3, hh3 = sig.freqz(np.array([1,0,-1]), [1])
ww3 = ww3 / np.pi

plt.figure(5)

plt.plot(ww3,(abs(hh3)))

plt.title('N=2')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo')
plt.grid(which='both', axis='both')



plt.figure(6)
plt.plot(ww3, 20 * np.log10(abs(hh3)))

plt.title('N=2')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

plt.show()

ww4, hh4 = sig.freqz(np.array([1,0,0,0,-1]), [1,0,1])
ww4 = ww4 / np.pi

plt.figure(7)

plt.plot(ww4,(abs(hh4)))

plt.title('N=4')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo')
plt.grid(which='both', axis='both')


plt.figure(8)
plt.plot(ww4, 20 * np.log10(abs(hh4)))


plt.title('N=4')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

plt.show()