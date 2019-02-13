from src.run_circuits import succes_probability
import matplotlib.pyplot as plt
import numpy as np

def cos_function(n):
    return (np.cos(np.pi/(2*n))**(2*n))

if __name__ == '__main__':

    x_sim = np.linspace(1,50,50)
    y_sim = cos_function(x_sim)
    x_axis = []
    y_axis = []
    for n in range(1,50,1):
        y_axis.append(succes_probability(100,n))
        x_axis.append(n)

    plt.plot(x_axis, y_axis,x_sim,y_sim)
    plt.ylabel('probability of detecting a live bomb')
    plt.xlabel('number of rotations')
    plt.show()

