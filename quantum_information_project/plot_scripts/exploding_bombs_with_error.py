from src.run_circuits import succes_probability
from matplotlib import pyplot as plt 
import numpy as np 

def bit_flip_channel(n,error_rate):
    return (((np.cos(np.pi/(2*n))**2) - error_rate*(np.cos(np.pi/n)))**n)

if __name__ == '__main__':

    error_range = [0.0001,0.001, 0.01, 0.05, 0.1, 0.2 , 0.3]
    xdata_list = np.zeros((7,50))
    ydata_list = np.zeros((7,50))
    x_func = np.linspace(1,50,50)
    y_func = np.zeros((7,50))    

    for i in range(len(error_range)):
        x_axis = []
        y_axis = []

        for n in range(1,51,1):
            y_axis.append(succes_probability(100,n,error_range[i]))
            x_axis.append(n)
            
        y_func[i,:] = bit_flip_channel(x_func,error_range[i])

        xdata_list[i,:] = x_axis
        ydata_list[i,:] = y_axis

    for i in range(len(error_range)):
        plt.plot(xdata_list[i,:], ydata_list[i,:])
    plt.legend(error_range)
    for i in range(len(error_range)):
        plt.plot(xdata_list[i,:], y_func[i,:],'b--', linewidth=0.5)
    plt.ylabel('probability of  measuring +1')
    plt.xlabel('number of rotation gates')

plt.show()
