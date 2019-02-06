from src.run_circuits import succes_probability
from matplotlib import pyplot as plt 
import numpy as np 

if __name__ == '__main__':
    error_range = [0.01, 0.05, 0.1, 0.2 , 0.3]
    xdata_list = np.zeros((5,25))
    ydata_list = np.zeros((5,25))
    for i in range(len(error_range)):
        x_axis = []
        y_axis = []
        for n in range(1,26,1):
            y_axis.append(succes_probability(10,n,error_range[i]))
            x_axis.append(n)

        xdata_list[i,:] = x_axis
        ydata_list[i,:] = y_axis
    
    error_bar = np.ones(25)/np.sqrt(100)
    for i in range(len(error_range)):
        plt.figure()
        plt.errorbar(xdata_list[i,:], ydata_list[i,:],error_bar)

        plt.ylabel('probability measuring 0')
        plt.xlabel('number of rotation gates')
        plt.legend(error_range[i])

    for k in plt.get_fignums():
        plt.figure(k)
        plt.show()
