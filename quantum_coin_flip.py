# Import necessary libraries
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def quantum_coin_flip(num_flips):
    """Simulates a quantum coin flip using a Hadamard gate."""
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Apply Hadamard gate to create superposition
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    
    # Use the Qiskit AerSimulator
    simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, simulator)
    
    # Run the simulation multiple times
    result = simulator.run(transpiled_qc, shots=num_flips).result()
    
    # Get the measurement results
    counts = result.get_counts()
    
    return counts

def plot_results(counts):
    """Plots the results of the quantum coin flip."""
    plt.bar(counts.keys(), counts.values(), color=['blue', 'red'])
    plt.xlabel('Coin Flip Result')
    plt.ylabel('Frequency')
    plt.title('Quantum Coin Flip Results')
    plt.xticks(['0', '1'], labels=['Heads (0)', 'Tails (1)'])
    plt.show()

if __name__ == "__main__":
    num_flips = 1000  # Number of quantum coin flips
    counts = quantum_coin_flip(num_flips)
    print(f"Quantum Coin Flip Results: {counts}")
    plot_results(counts)
