import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.signal as sig


K = 4096  # length of random signal
N = 3  # order of AR model
a = np.array((1, -1, .5))  # coefficients of AR model

# generate random signal n[k]
np.random.seed(2)
n = np.random.normal(size=K)

# AR model for random signal x[k]
x = np.zeros(K)
for k in np.arange(3, K):
    x[k] = a[0]*x[k-1] + a[1]*x[k-2] + a[2]*x[k-3] + n[k]
    
# estimate AR parameters by Yule-Walker method
rho, sigma = sm.regression.yule_walker(x, order=N, method='mle')

# compute true and estimated transfer function
Om, H = sig.freqz(1, np.insert(-a, 0, 1))
Om, He = sig.freqz(1, np.insert(-rho, 0, 1))
# compute PSD by Welch method
Om2, Pxx = sig.welch(x, return_onesided=True)

# plot PSDs
plt.figure(figsize=(10,5))
plt.plot(Om, np.abs(H)**2, label=r'$\Phi_{xx}(e^{j\Omega})$')
plt.plot(Om2*2*np.pi, .5*np.abs(Pxx), 'k-', alpha=.5 , label=r'$\hat{\Phi}_{xx}(e^{j\Omega})$ (Welch)')
plt.plot(Om, np.abs(He)**2, label=r'$\hat{\Phi}_{xx}(e^{j\Omega})$ (parametric)')

plt.xlabel(r'$\Omega$')
plt.axis([0, np.pi, 0, 20])
plt.legend();

