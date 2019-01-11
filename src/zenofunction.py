import numpy as np
from matplotlib import pyplot as plt


K = 50
def zeno_function(n):
    return (1+ (1-2*np.sin(np.pi/2/n)**2)**(n))/2

x = np.linspace(1,K,K)
y = zeno_function(x)
plt.suptitle('Plot of the Quantum Zeno Effect')
plt.ylabel('probability of measuring 0')
plt.xlabel('number of rotations')

plt.plot(x,y)
plt.show()

