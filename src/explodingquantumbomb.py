from quantumbomb import quantum_bomb, rotation_angle, get_all_probabilities
from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator

def run_once_with_bombs_exploding(number_of_iterations, error = False):

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
        state_2 = get_all_probabilities(eng, q2)
        print(state_2, 'state qubit in bomb')
        if state_2 == [1]:
            print('booooom')
            break

    print('no bombs exploded')
    state_1 = get_all_probabilities(eng, q1)
    if state_1 == [0]:
        print('it was a real bomb!')
    Measure | q1
    Measure | q2
    return(state_1)

if __name__ == '__main__':
    run_once_with_bombs_exploding(10)
