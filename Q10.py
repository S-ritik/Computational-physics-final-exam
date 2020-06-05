# Q10 - To get the fourier transform of box function
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt


def f(x):   # Box function
    f = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < 1 and x[i] > -1:
            f[i] = 1
        else:
            f[i] = 0
    return f

def ft(n):
    x = np.linspace(-50, 50, n+1)
    dx= x[1]-x[0]
    y = f(x[0:n])
    y = fft.fftshift(y)           
    dft = fft.fftshift(fft.fft(y))
    k = 2*np.pi*fft.fftshift(fft.fftfreq(n,dx)) 
    ft = ((dx)/np.sqrt(2*np.pi))*np.real(dft)
    plt.subplot(221)
    plt.plot(k, ft,label="At sampling different sampling rates")
    plt.title('Fourier Transform of Box function')


ft(1024)
ft(512)
ft(2048)
x = np.linspace(-50, 50,1024)
plt.plot(x, f(x),label="Box function")
plt.legend()
plt.show()
