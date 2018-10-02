import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal


N = 1000
fs = 1000
a2 = 0.01

tt = np.linspace (0,((N-1)*(1/fs)),N)

O1 = np.pi /2
O2 = O1 + 10 *2*np.pi /N

x1 = np.sin(O1*tt)

x2 = a2*np.sin(O2*tt)

a = np.array(x1)
b = np.array(x2)

x = a + b

sp1 = np.fft.fft(x1)
plt.title('Señal X1' )
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.plot(tt,x1)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp1)[0:500]))
plt.show()
plt.stem(np.absolute(sp1)[0:500])
plt.show()


sp2 = np.fft.fft(x2)
plt.title('Señal X2' )
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.plot(tt,x2)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp2)[0:500]))
plt.show()
plt.stem(np.absolute(sp2)[0:500])
plt.show()


sp3 = np.fft.fft(x)
plt.title('Señal X' )
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.plot(tt,x)
plt.show()
plt.title('Espectro' )
plt.ylabel("Magnitud [dB]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp3)[0:500]))
plt.show()
plt.stem(np.absolute(sp3)[0:500])
plt.show()

ma = np.absolute(sp3)[0:500]
asd = max(ma)


count = -1
for x in ma:
    count = 1+count   
    if x == asd:       
        frec = count
        





