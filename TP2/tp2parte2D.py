import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal

def Rectangular (N,x):
    
    ventana = signal.boxcar(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Bartlett (N,x):
    
    ventana = signal.bartlett(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Hann (N,x):
    
    ventana = signal.windows.hann(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Blackman (N,x):
    
    ventana = signal.blackman(N)
    
    salida = np.multiply(x,ventana)

    return salida

def Flattop (N,x):
    
    ventana = signal.flattop(N)
    
    salida = np.multiply(x,ventana)

    return salida

N = 1000
fs = 1000
tt = np.linspace (0,((N-1)*(1/fs)),N)

################################################
AmplitudB = [110,120,130,285,300]

ArrayB = np.array([AmplitudB])

a2B = 10**(-ArrayB/20)
O1B = 2*np.pi*(fs/4)
O2B = O1B + 10*2*np.pi

x1B = np.sin(O1B*tt)

x2B = a2B.T*np.sin(O2B*tt)

xB = x1B + x2B
#################################################
AmplitudC = [30,20,30,35]

ArrayC = np.array([AmplitudC])

a2C = 10**(-ArrayC/20)
O1C = 2*np.pi*(fs/4) + 0.5*2*np.pi
O2C = O1C + 10 *2*np.pi

x1C = np.sin(O1C*tt)

x2C = a2C.T*np.sin(O2C*tt)

xC = x1C + x2C
#################################################

rectangularB = Rectangular(N,xB)
bartlettB = Bartlett(N,xB)
hannB     = Hann(N,xB)
blackmanB = Blackman(N,xB)
flattopB  = Flattop(N,xB)

sp0B = np.fft.fft(rectangularB)
sp1B = np.fft.fft(bartlettB)
sp2B = np.fft.fft(hannB)
sp3B = np.fft.fft(blackmanB)
sp4B = np.fft.fft(flattopB)

plt.title('Ventana rectangular con -300db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp0B[4,])[200:300]))
plt.show()

plt.title('Ventana bartlett con -285db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp1B[3,])[200:300]))
plt.show()

plt.title('Ventana hanning con -110db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp2B[0,])[200:300]))
plt.show()

plt.title('Ventana blackman con -120db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp3B[1,])[200:300]))
plt.show()

plt.title('Ventana flat-top con -130db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.plot(20*np.log10(np.absolute(sp4B[2,])[200:300]))
plt.show()
###################################################
rectangularC = Rectangular(N,xC)
bartlettC = Bartlett(N,xC)
hannC     = Hann(N,xC)
blackmanC = Blackman(N,xC)
flattopC  = Flattop(N,xC)

sp0C = np.fft.fft(rectangularC)
sp1C = np.fft.fft(bartlettC)
sp2C = np.fft.fft(hannC)
sp3C = np.fft.fft(blackmanC)
sp4C = np.fft.fft(flattopC)

plt.title('Ventana rectangular con -30db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.stem((np.absolute(sp0C[0,])[240:270]))
plt.show()

plt.title('Ventana bartlett con -30db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.stem((np.absolute(sp1C[0,])[240:270]))
plt.show()

plt.title('Ventana hanning con -asddb30db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.stem((np.absolute(sp2C[0,])[240:270]))
plt.show()

plt.title('Ventana blackman con -30db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.stem((np.absolute(sp3C[0,])[240:270]))
plt.show()

plt.title('Ventana flat-top con -30db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
plt.stem((np.absolute(sp4C[0,])[240:270]))
plt.show()










































