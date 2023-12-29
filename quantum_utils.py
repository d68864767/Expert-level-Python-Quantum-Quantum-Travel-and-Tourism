```python
import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram

def create_quantum_circuit(num_qubits, num_bits):
    """
    Function to create a quantum circuit
    """
    qc = QuantumCircuit(num_qubits, num_bits)
    return qc

def apply_hadamard(qc, qubit):
    """
    Function to apply a Hadamard gate
    """
    qc.h(qubit)
    return qc

def apply_measurement(qc, qubit, bit):
    """
    Function to apply a measurement
    """
    qc.measure(qubit, bit)
    return qc

def run_circuit(qc):
    """
    Function to run the quantum circuit
    """
    simulator = Aer.get_backend('qasm_simulator')
    transpiled_circuit = transpile(qc, simulator)
    qobj = assemble(transpiled_circuit)
    result = simulator.run(qobj).result()
    return result.get_counts(qc)

def visualize_circuit(qc):
    """
    Function to visualize the quantum circuit
    """
    return qc.draw()

def visualize_counts(counts):
    """
    Function to visualize the counts
    """
    return plot_histogram(counts)

def visualize_bloch(qc):
    """
    Function to visualize the Bloch vector
    """
    simulator = Aer.get_backend('statevector_simulator')
    statevector = execute(qc, simulator).result().get_statevector()
    return plot_bloch_multivector(statevector)
```
