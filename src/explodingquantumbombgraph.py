from explodingquantumbomb import succes_probability
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_axis = []
    y_axis = []
    for n in range(1,50,1):
        y_axis.append(succes_probability(100,n))
        x_axis.append(n)
    plt.plot(x_axis, y_axis)    
    plt.ylabel('probability of detecting a bomb (with exploding')
    plt.xlabel('number of rotation gates')
plt.show()
