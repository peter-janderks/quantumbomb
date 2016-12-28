from projectq.setups.ibm import IBMBackend
from projectq.ops import Measure, Entangle
from projectq import MainEngine


def run_entangle(eng, num_qubits=3):
	"""
	Runs an entangling operation on the provided compiler engine.
	
	Args:
		eng (MainEngine): Main compiler engine to use.
		num_qubits (int): Number of qubits to entangle.
	
	Returns:
		measurement (list<int>): List of measurement outcomes.
	"""
	# allocate the quantum register to entangle
	qureg = eng.allocate_qureg(num_qubits)

	# entangle the qureg
	Entangle | qureg
	
	# measure; should be all-0 or all-1
	Measure | qureg
	
	# run the circuit
	eng.flush()
	
	# return the list of measurements
	return [int(q) for q in qureg]


if __name__ == "__main__":
	# create main compiler engine for the IBM back-end
	eng = MainEngine(IBMBackend(use_hardware=True, num_runs=1024, verbose=True))
	# run the circuit and print the result
	print(run_entangle(eng))
