from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator

import random
import numpy

def quantum_bomb(eng, qubit_a, qubit_b):
    CNOT | (qubit_a, qubit_b)
    Measure | qubit_b
    return(qubit_a, qubit_b)

def pauli_error(eng, qubit_a, error_rate):
    if random.random() < error_rate:
        X | qubit_a
    return(qubit_a)
