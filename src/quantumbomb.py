from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator

import random
import numpy 

def rotation_angle(number_of_rotations):
    rotation_angle = (numpy.pi) / (number_of_rotations)
    return(rotation_angle)

def quantum_bomb(eng, qubit_a, qubit_b):    
    CNOT | (qubit_a, qubit_b)
    Measure | qubit_b
    
    return(qubit_a, qubit_b)

def pauli_error(eng, qubit_a, error_rate):
    if random.random() < error_rate:
        rand_num = random.random()
        if rand_num < 1/3:
            X | qubit_a
            print('ERROR')
        elif rand_num > 2/3:
            Y | qubit_a
        else:
            Z | qubit_a

    return(qubit_a)

def get_all_probabilities(eng,qureg):
    i = 0
    y = len(qureg)
    while i < (2**y):
        qubit_list = [int(x) for x in list(('{0:0b}'.format(i)).zfill(y))]
        qubit_list = qubit_list[::-1]
        l = eng.backend.get_probability(qubit_list,qureg)
        if l != 0.0:
            return(qubit_list)
        i += 1     
            
def run_once_without_bombs_exploding(number_of_iterations, error = False):
    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()
    error_on = error
    error_rate = 0.1
    angle = rotation_angle(number_of_iterations)

    for _ in range(0,number_of_iterations):
        Rx(angle) | q1
        quantum_bomb(eng,q1,q2)
        if error_on == True:
            pauli_error(eng,q1,error_rate)
        
        eng.flush()

    state = get_all_probabilities(eng, q1)
    Measure | q1
    Measure | q2
    return(state)

def state_count(iterations_of_circuit, rotation_iterations = 5):
    state_count_0 = 0
    state_count_1 = 1

    for _ in range(0,iterations_of_circuit):
        x = run_once_without_bombs_exploding(rotation_iterations)
        if x == [0]:
            state_count_0 += 1
        else:
            state_count_1 += 1
    return(state_count_0)        
    print(state_count_0, 'times 0 was measured')

def state_probability(iterations_of_circuit, rotation_iterations = 5):
    state_count_0 = state_count(iterations_of_circuit, rotation_iterations)
    print(state_count_0/iterations_of_circuit, 'times 0 was measured')
    return(state_count_0/iterations_of_circuit)


if __name__ == '__main__':
    state_count(500)
