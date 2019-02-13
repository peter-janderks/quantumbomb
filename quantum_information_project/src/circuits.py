from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator
from .gates import quantum_bomb, pauli_error
from .util import rotation_angle, get_all_probabilities

import random
import numpy

def circuit_without_bombs_exploding(number_of_iterations, noise = False, error_rate = 0):
    
    # allocate qubits and initialize engine
    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()

    angle = rotation_angle(number_of_iterations)

    for _ in range(0,number_of_iterations):
        
        if noise == True:
            pauli_error(eng,q1,error_rate)

        # rotate qubit and send through bomb   
        Rx(angle) | q1
        quantum_bomb(eng,q1,q2)
        
    state = get_all_probabilities(eng, q1)
    Measure | q1
    Measure | q2
    eng.flush()
    return(state)

def circuit_with_bombs_exploding(number_of_iterations, error_rate = 0):

    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()
    angle = rotation_angle(number_of_iterations)
    errors = 0

    for x in range(0,number_of_iterations):

        if error_rate != 0:
            q1 = pauli_error(eng,q1,error_rate)
        
        # rotate qubit and send through bomb  
        Rx(angle) | q1
        quantum_bomb(eng,q1,q2)
        eng.flush()        
        state_2 = get_all_probabilities(eng, q2)
        
        # if the qubit in the bomb is measured in the state |1> the bomb 
        # explodes
        if state_2 == [1]:
            print('booooom')
            Measure | q1
            Measure | q2
            return('fail')
            break

    # if the bomb does not explode and one is measured at the end, then a real
    # bomb has been succesfully detected
    state_1 = get_all_probabilities(eng, q1)

    Measure | q1
    Measure | q2
    
    if state_1 == [0]:
        print('succes, you found a real bomb!')
        print('no bombs exploded')
        return('succes')
    
