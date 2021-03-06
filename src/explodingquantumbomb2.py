from quantumbomb import quantum_bomb, rotation_angle, get_all_probabilities, pauli_error
from projectq.ops import H, Measure, X, Rx, CNOT, Y, Z
from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator

def run_once_with_bombs_exploding(number_of_iterations, error_rate = 0.0):

    eng = MainEngine()
    q1 = eng.allocate_qubit()
    q2 = eng.allocate_qubit()
    angle = rotation_angle(number_of_iterations)


    for x in range(0,number_of_iterations):
        Rx(angle) | q1
        quantum_bomb(eng,q1,q2)
        if error_rate > 0.0:
            pauli_error(eng,q1,error_rate)

        eng.flush()
        state_2 = get_all_probabilities(eng, q2)
        print(state_2, 'state qubit in bomb')
        if state_2 == [1]:
            print('booooom')
            break
    state_1 = get_all_probabilities(eng, q1)    

    Measure | q1
    Measure | q2

    if x == number_of_iterations-1 and state_1 == [0]:
        print('succes, you found a real bomb!')
        print('no bombs exploded')
        return('succes')
    
    return('fail')

def succes_probability(iterations_of_circuit, error, rotation_iterations):
    succes_count = 0
    for _ in range(0,iterations_of_circuit):
        x = run_once_with_bombs_exploding(rotation_iterations, error)
        if x == 'succes':
            succes_count += 1
    succes_prob = succes_count/iterations_of_circuit
    print(succes_prob, 'times 0 was measured')
    return(succes_prob)

if __name__ == '__main__':
    run_once_with_bombs_exploding(10, error_rate = 0.01)

    print(succes_probability(10,10))
