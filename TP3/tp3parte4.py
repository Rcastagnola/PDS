import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integrate
import scipy.signal as sig
import spectrum as sp
import warnings
warnings.filterwarnings('ignore')

def Bartlett (N,x):
    
    ventana = sig.bartlett(N)
    
    salida = np.multiply(x,ventana)

    return salida

def normalize(d):
    # d is a (n x dimension) np array
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d


N = 1000
fs = 1000

tt = np.linspace (0,((N-1)*(1/fs)),N)

Repeticiones = 200

a3db = 0.20

frecA = np.zeros(Repeticiones)
Acumulado3dbA = np.zeros(1000)
Acumulado3dbB = np.zeros(1000)

for h in range(Repeticiones):
        ruidoA = np.random.normal(0,2,N)
        frA = np.random.uniform(-0.5, 0.5, 1)
        O0A = 2*np.pi*(fs/4)
        O1A = O0A + frA*2*np.pi
        senoidalA = a3db*np.sin(O1A*tt) 
        señalA = senoidalA + ruidoA
        
        Sen3db = np.absolute(np.fft.fft(senoidalA))
        
        Rui3db = np.absolute(np.fft.fft(ruidoA))
        
        _, PxxSeñalA = sig.welch(señalA, fs=fs, nfft=N, window='bartlett', nperseg=int(np.round(N/3)) )        
        
        MaxfrecA = max(PxxSeñalA)
        countA = -1
        for x in PxxSeñalA:
            countA = 1+countA   
            if x == MaxfrecA:       
                frecA[h] = countA
        
        Acumulado3dbA = Sen3db + Acumulado3dbA
        Acumulado3dbB = Rui3db + Acumulado3dbB

SenProm3db = Acumulado3dbA / Repeticiones 
RuiProm3db = Acumulado3dbB / Repeticiones
       
plt.figure(1)
plt.title('Amp 0.2 - 3db')
plt.plot(20*np.log10(SenProm3db[240:260]),label='Senoidal')
plt.plot(20*np.log10(RuiProm3db[240:260]),label='Ruido')
axes_hdl = plt.gca()
axes_hdl.legend()
        
maximoSen3db = max(20*np.log10(SenProm3db))
maximoRui3db = max(20*np.log10(RuiProm3db))
        
        
varianceA = np.var(frecA)

SesgoA = sum(frecA - 250) / 200



#################################################################

frecB = np.zeros(Repeticiones)

for j in range(Repeticiones):
        ruidoB = np.random.normal(0,2,N)
        frB = np.random.uniform(-0.5, 0.5, 1)
        O0B = 2*np.pi*(fs/4)
        O1B = O0B + frB*2*np.pi
        senoidalB = a3db*np.sin(O1B*tt)
        señalB = senoidalB + ruidoB            
    
        pARMASeñalB = sp.parma(señalB, 8, 8, 30, NFFT=N)
            
        MaxfrecB = max(pARMASeñalB.psd)
        countB = -1
        for y in pARMASeñalB.psd:
            countB = 1+countB   
            if y == MaxfrecB:       
                frecB[j] = countB
        
               
varianceB = np.var(frecB)   

SesgoB = sum(frecB - 250) / 200
    
###################################################################    

a10db = 0.45

frecC = np.zeros(Repeticiones)
Acumulado10dbA = np.zeros(1000)
Acumulado10dbB = np.zeros(1000)

for k in range(Repeticiones):
        ruidoC = np.random.normal(0,2,N)
        frC = np.random.uniform(-0.5, 0.5, 1)
        O0C = 2*np.pi*(fs/4)
        O1C = O0C + frC*2*np.pi
        senoidalC = a10db*np.sin(O1C*tt) 
        señalC = senoidalC + ruidoC
        
        Sen10db = np.absolute(np.fft.fft(senoidalC))
        
        Rui10db = np.absolute(np.fft.fft(ruidoC))
        
        _, PxxSeñalC = sig.welch(señalC, fs=fs, nfft=N, window='bartlett', nperseg=int(np.round(N/3)) )        
        
        MaxfrecC = max(PxxSeñalC)
        countC = -1
        for z in PxxSeñalC:
            countC = 1+countC   
            if z == MaxfrecC:       
                frecC[k] = countC
        
        Acumulado10dbA = Sen10db + Acumulado10dbA
        Acumulado10dbB = Rui10db + Acumulado10dbB

SenProm10db = Acumulado10dbA / Repeticiones 
RuiProm10db = Acumulado10dbB / Repeticiones
       
plt.figure(2)
plt.title('Amp 0.45 - 10db')
plt.plot(20*np.log10(SenProm10db[240:260]),label='Senoidal')
plt.plot(20*np.log10(RuiProm10db[240:260]),label='Ruido')
axes_hdl = plt.gca()
axes_hdl.legend()
        
maximoSen10db = max(20*np.log10(SenProm10db))
maximoRui10db = max(20*np.log10(RuiProm10db))
        
        
varianceC = np.var(frecC) 

SesgoC = sum(frecC - 250) / 200 

####################################################################

frecD = np.zeros(Repeticiones)

for l in range(Repeticiones):
        ruidoD = np.random.normal(0,2,N)
        frD = np.random.uniform(-0.5, 0.5, 1)
        O0D = 2*np.pi*(fs/4)
        O1D = O0D + frD*2*np.pi
        senoidalD = a10db*np.sin(O1D*tt)
        señalD = senoidalD + ruidoD            
    
        pARMASeñalD = sp.parma(señalD, 8, 8, 30, NFFT=N)
    
        MaxfrecD = max(pARMASeñalD.psd)
        countD = -1
        for w in pARMASeñalD.psd:
            countD = 1+countD   
            if w == MaxfrecD:       
                frecD[l] = countD
        
               
varianceD = np.var(frecD)

SesgoD = sum(frecD - 250) / 200






