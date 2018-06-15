from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-1, 1, 200, endpoint=False)
sig  = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc=2)
widths = np.arange(1, 31)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
print(cwtmatr.shape)
plt.imshow(cwtmatr)
# plt.plot(t,sig);
plt.show()