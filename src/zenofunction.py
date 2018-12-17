import numpy as np
from matplotlib import pyplot as plt


K = 100
def zeno_function(n):
    return (1+ (1-2*np.sin(np.pi/2/n)**2)**(n))/2

x = np.linspace(1,K,K)

y = zeno_function(x)

#plt.plot(x,y)
#plt.show()

