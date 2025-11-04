from qiskit.providers.aer import AerSimulator
from qiskit.algorithms import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit_optimization.applications import Maxcut
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.utils import QuantumInstance
import networkx as nx


# Define problem graph
graph = nx.Graph()
graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

# Create MaxCut problem
maxcut = Maxcut(graph)
qp = maxcut.to_quadratic_program()

# Backend and QuantumInstance
backend = AerSimulator()
quantum_instance = QuantumInstance(backend)

# Optimizer and QAOA
optimizer = COBYLA(maxiter=100)
qaoa = QAOA(optimizer=optimizer, reps=1, quantum_instance=quantum_instance)

# MinimumEigenOptimizer
meo = MinimumEigenOptimizer(qaoa)

# Solve problem
result = meo.solve(qp)

# Print results
print("Optimal value:", result.fval)
print("Optimal solution:", result.x)
