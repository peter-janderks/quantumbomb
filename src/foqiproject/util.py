from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator
import numpy

# returns an array containing the probability of measuring a quantum register
# in a certain quantum state. Only includes states with a non-zero 
# probability 
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

# calculates the angle with which the qubit is rotated each iteration
def rotation_angle(number_of_rotations):
    rotation_angle = (numpy.pi) / (number_of_rotations)
    return(rotation_angle)

