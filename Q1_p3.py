# Import necessary modules
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_state_city
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gates to both qubits
qc.h(0)
qc.h(1)

# Apply Pauli-Z gate to the second qubit
qc.z(0)

# Draw the quantum circuit
qc.draw('text')  # You can also use 'text' if mpl doesn't work
plt.show()

# Simulate the circuit using Aer simulator
backend = Aer.get_backend('statevector_simulator')
job = backend.run(qc)
result = job.result()
statevector = result.get_statevector()

# Print the final statevector
print("Final statevector:")
print(statevector)

# Visualize the statevector using a cityscape plot
plot_state_city(statevector, title="Final Quantum State")
plt.show()
