# The tools we will need
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
# Qiskit allows us to make beautiful plots
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# allows us to do quantum simulation of measurements
M_simulator = Aer.backends(name='qasm_simulator')[0]

qreg = QuantumRegister(2)  # qreg is filled with two qubits
creg = ClassicalRegister(2)  # creg is filled with two classical bits

# we put our qreg and creg together to make our Quantum Circuit, called entangler here.
entangler = QuantumCircuit(qreg, creg)


entangler.h(0) # Apply the Hadamard gate to the first qubit
entangler.cx(0,1) # Apply the CNOT gate with the first qubit as the control and second qubit as the target

entangler.measure(0,0) # measure the first qubit and record it in the first classical bit
entangler.measure(1,1) # measure the second qubit and record it in the second classical bit

#executes numerous measurements
job = execute(entangler, M_simulator)
#gives us histogram results
hist = job.result().get_counts()
#plot a stunning visualization
plot_histogram(data=hist, title="Maximally Entangled State")
plt.show()