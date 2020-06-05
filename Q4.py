# Q4 - To compute the power spectrum

import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt
from scipy import stats

# To create a random sample
randno=np.random.uniform(0,1,1024)

# To plot the random sample
plt.plot(randno,'cyan',label="Sample")
plt.xlabel("ith element of sample")
plt.ylabel("Value of element of sample")
plt.legend()
plt.show()

# To compute power spectrum of it
randnofft=np.fft.fft(randno)
powspect=np.square(np.abs(randnofft))/(1024*np.pi*2)
powspect=np.fft.fftshift(powspect)
freq=np.fft.fftshift(np.fft.fftfreq(1024))
plt.plot(freq,powspect)
plt.ylabel('Power Spectrum')
plt.xlabel("Frequency")
plt.show()

k_bin, pdg_bin, binnumber= stats.binned_statistic(freq, powspect, bins= 5)
av_pdg_bin=(pdg_bin[0:len(pdg_bin)-1]+pdg_bin[1:len(pdg_bin)])/2
plt.bar(av_pdg_bin, k_bin, width=pdg_bin[1]-pdg_bin[0])
plt.ylabel('Power Spectrum')
plt.xlabel("Frequency")
plt.show()
