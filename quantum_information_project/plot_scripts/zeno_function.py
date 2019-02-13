import numpy as np
from matplotlib import pyplot as plt
from src.run_circuits import state_probability
K = 50
x_axis = []
y_axis = []

def zeno_function(n):
    return (1+ (1-2*np.sin(np.pi/2/n)**2)**(n))/2

for n in range(1,51,1):
    y_axis.append(state_probability(100,n))
    x_axis.append(n)

x = np.linspace(1,K,K)
y = zeno_function(x)
plt.ylabel('probability of measuring +1')
plt.xlabel('number of rotations')

plt.plot(x,y, x_axis, y_axis)
plt.show()

