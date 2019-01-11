from quantumbomb import state_probability
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    x_axis = []
    y_axis = []
    for n in range(1,50,1):
        y_axis.append(state_probability(200,n))
        x_axis.append(n)
    plt.suptitle('Plot of the circuit simulation of the Quantum Zeno Effect')
    plt.plot(x_axis, y_axis)    
    plt.ylabel('probability of measuring 0')
    plt.xlabel('number of rotations')
    plt.show()
#    plt.plot([1,2,3,4])
#    plt.ylabel('some numbers')
#    plt.show()
