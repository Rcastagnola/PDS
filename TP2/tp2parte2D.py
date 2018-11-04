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

def normalize(d):
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d

N = 1000
fs = 1000
tt = np.linspace (0,((N-1)*(1/fs)),N)

################################################
AmplitudBEj2D = [110,120,130,285,300]

ArrayBEj2D = np.array([AmplitudBEj2D])

a2BEj2D = 10**(-ArrayBEj2D/20)
O1BEj2D = 2*np.pi*(fs/4)
O2BEj2D = O1BEj2D + 10*2*np.pi

x1BEj2D = np.sin(O1BEj2D*tt)

x2BEj2D = a2BEj2D.T*np.sin(O2BEj2D*tt)

xBEj2D = x1BEj2D + x2BEj2D
#################################################
AmplitudCEj2D = [50,60,70,80,90,100,110,120]

ArrayCEj2D = np.array([AmplitudCEj2D])

a2CEj2D = 10**(-ArrayCEj2D/20)
O1CEj2D = 2*np.pi*(fs/4) + 0.5*2*np.pi
O2CEj2D = O1CEj2D + 10 *2*np.pi

x1CEj2D = np.sin(O1CEj2D*tt)

x2CEj2D = a2CEj2D.T*np.sin(O2CEj2D*tt)

xCEj2D = x1CEj2D + x2CEj2D
#################################################

rectangularBEj2D = Rectangular(N,xBEj2D)
bartlettBEj2D = Bartlett(N,xBEj2D)
hannBEj2D     = Hann(N,xBEj2D)
blackmanBEj2D = Blackman(N,xBEj2D)
flattopBEj2D  = Flattop(N,xBEj2D)

sp0BEj2D = np.fft.fft(rectangularBEj2D)
sp1BEj2D = np.fft.fft(bartlettBEj2D)
sp2BEj2D = np.fft.fft(hannBEj2D)
sp3BEj2D = np.fft.fft(blackmanBEj2D)
sp4BEj2D = np.fft.fft(flattopBEj2D)

plt.title('Ventana rectangular con -300db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp0BEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp0BEj2D[4,]))])))
plt.plot(Nsp0BEj2D[200:300])
plt.show()

plt.title('Ventana bartlett con -285db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp1BEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp1BEj2D[3,]))])))
plt.plot(Nsp1BEj2D[200:300])
plt.show()

plt.title('Ventana hanning con -110db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp2BEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp2BEj2D[0,]))])))
plt.plot(Nsp2BEj2D[200:300])
plt.show()

plt.title('Ventana blackman con -120db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp3BEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp3BEj2D[1,]))])))
plt.plot(Nsp3BEj2D[200:300])
plt.show()

plt.title('Ventana flat-top con -130db' )
plt.ylabel("Magnitud [db]")
plt.xlabel("Frequencia")
Nsp4BEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp4BEj2D[2,]))])))
plt.plot(Nsp4BEj2D[200:300])
plt.show()
###################################################
rectangularCEj2D = Rectangular(N,xCEj2D)
bartlettCEj2D = Bartlett(N,xCEj2D)
hannCEj2D     = Hann(N,xCEj2D)
blackmanCEj2D = Blackman(N,xCEj2D)
flattopCEj2D  = Flattop(N,xCEj2D)

sp0CEj2D = np.fft.fft(rectangularCEj2D)
sp1CEj2D = np.fft.fft(bartlettCEj2D)
sp2CEj2D = np.fft.fft(hannCEj2D)
sp3CEj2D = np.fft.fft(blackmanCEj2D)
sp4CEj2D = np.fft.fft(flattopCEj2D)

plt.title('Ventana rectangular con -50db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp0CEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp0CEj2D[0,]))])))
plt.plot((Nsp0CEj2D[240:270]))
plt.show()

plt.title('Ventana bartlett con -60db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp1CEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp1CEj2D[1,]))])))
plt.plot((Nsp1CEj2D[240:270]))
plt.show()

plt.title('Ventana hanning con -80db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp2CEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp2CEj2D[3,]))])))
plt.plot((Nsp2CEj2D[240:270]))
plt.show()

plt.title('Ventana blackman con -90db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp3CEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp3CEj2D[4,]))])))
plt.plot((Nsp3CEj2D[240:270]))
plt.show()

plt.title('Ventana flat-top con -120db' )
plt.ylabel("Magnitud")
plt.xlabel("Frequencia")
Nsp4CEj2D = 20*np.log10(np.transpose(([normalize(np.absolute(sp4CEj2D[7,]))])))
plt.plot((Nsp4CEj2D[240:270]))
plt.show()