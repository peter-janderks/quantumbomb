from src.run_circuits import succes_probability
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_axis = []
    y_axis = []
    
    # running the circuit for 50 different angles
    for n in range(1,50,1):
        # for each angle the circuit is run 100 times
        y_axis.append(succes_probability(100,n))
        x_axis.append(n)
    plt.plot(x_axis, y_axis)
    plt.ylabel('probability of detecting a bomb (with exploding')
    plt.xlabel('number of rotation gates')

def cos_function(n):
    return (np.cos(np.pi/(2*n))**n)
plt.show()