from projectq.ops import H, Measure, X, Rx, CNOT
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator

import numpy 

def rotation_angle(number_of_rotations):
    rotation_angle = (numpy.pi) / (number_of_rotations)
#    print(rotation_angle, "rotation angle")
    return(rotation_angle)

def quantum_bomb(eng, qubit_a, qubit_b):    
    CNOT | (qubit_a, qubit_b)
    Measure | qubit_b
    return(qubit_a, qubit_b)

def get_all_probabilities(eng,qureg):
    i = 0
    y = len(qureg)
    while i < (2**y):
        qubit_list = [int(x) for x in list(('{0:0b}'.format(i)).zfill(y))]
        qubit_list = qubit_list[::-1]
        l = eng.backend.get_probability(qubit_list,qureg)
        if l != 0.0:
#            print("probability:", l,"state:", qubit_list)
            return(qubit_list)
        i += 1     
            
def run_once():
    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()
    number_of_iterations = 5
    angle = rotation_angle(number_of_iterations)

    for num in range(0,number_of_iterations):
        Rx(angle) | q1
 
        quantum_bomb(eng,q1,q2)
        eng.flush()

    state = get_all_probabilities(eng, q1)
    Measure | q1
    Measure | q2
    return(state)

def state_count(iterations):
    state_count_0 = 0
    state_count_1 = 1

    for i in range(0,iterations):
        x = run_once()
        if x == [0]:
            state_count_0 += 1
        else:
            state_count_1 += 1
            
    print(state_count_0, 'times 0 was measured')

if __name__ == '__main__':
    state_count(5000)
