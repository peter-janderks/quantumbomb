from quantumbomb import state_probability
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    x_axis = []
    y_axis = []
    for n in range(1,25,5):
        y_axis.append(state_probability(100,n))
        x_axis.append(n)
    plt.plot(x_axis, y_axis)    
    plt.ylabel('probability measuring 0')
    plt.xlabel('number of rotation gates')
    plt.show()
#    plt.plot([1,2,3,4])
#    plt.ylabel('some numbers')
#    plt.show()
