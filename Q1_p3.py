from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gates to both qubits
qc.h(0)
qc.h(1)

# Apply Pauli-Z gate to the second qubit
qc.z(1)

# Draw the quantum circuit
qc.draw('mpl')  # You can also use qc.draw() if mpl is unavailable
plt.show()

# Simulate the final statevector
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
statevector = result.get_statevector()

# Print the final statevector
print("Final statevector:")
print(statevector)

# Plot the statevector as a cityscape (amplitude + phase)
plot_state_city(statevector, title="Final Quantum State")
plt.show()

# Optional: Plot Bloch vectors for individual qubits
plot_bloch_multivector(statevector)
plt.show()