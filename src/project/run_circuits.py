from projectq import MainEngine
from projectq.backends._sim._simulator import Simulator
from circuits import circuit_without_bombs_exploding


# runs the circuit without bombs exploding multiple times and keeps track of
# the number of times the qubit sent through the bomb is in state 0 and in 
# state 1                                                           
def state_count(iterations_of_circuit, rotation_iterations = 5):
    state_count_0 = 0
    state_count_1 = 1

    for _ in range(0,iterations_of_circuit):
        x = circuit_without_bombs_exploding(rotation_iterations)
        if x == [0]:
            state_count_0 += 1
        else:
            state_count_1 += 1
    return(state_count_0)
    print(state_count_0, 'times 0 was measured')

# runs the circuit multiple times using the state_count function. Calculates
# the average probability of measuring 0 or 1 at the end of the circuit       

def state_probability(iterations_of_circuit, rotation_iterations = 5):
    state_count_0 = state_count(iterations_of_circuit, rotation_iterations)
    print(state_count_0/iterations_of_circuit, 'times 0 was measured')
    return(state_count_0/iterations_of_circuit)
