from quantumbomb import state_probability
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    for n in range(1,100):
        state_probability(100,n)

#    plt.plot([1,2,3,4])
#    plt.ylabel('some numbers')
#    plt.show()
