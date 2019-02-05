from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator
from gates import quantum_bomb, pauli_error
from util import rotation_angle, get_all_probabilities

import random
import numpy

def circuit_without_bombs_exploding(number_of_iterations, error = False, error_rate = 0):
    
    # allocate qubits and initialize engine
    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()

    angle = rotation_angle(number_of_iterations)

    for _ in range(0,number_of_iterations):
        
        # rotate qubit and send through bomb
        Rx(angle) | q1
        quantum_bomb(eng,q1,q2)
        
        if error == True:
            pauli_error(eng,q1,error_rate)

        eng.flush()
    
    state = get_all_probabilities(eng, q1)
    Measure | q1
    Measure | q2
    return(state)

