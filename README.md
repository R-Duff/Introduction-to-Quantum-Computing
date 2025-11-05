# An Introduction to Quantum Error Correction

This is an evolving project demonstrating quantum error correction techniques using Qiskit. The intention in making this project is to continue adding to it, but for now it contains bit flip checking and Shor Code demonstration. The project simulates the encoding, random bit-flip error, detection, and correction of a single qubit using the 3-qubit bit-flip code, and then also the Shor Code approach.

## What It Shows

- Creation of a logical qubit in superposition (`|+⟩`)
- Encoding using the 3-qubit repetition code
- Random injection of a bit-flip error on one of the qubits
- Syndrome measurement using ancilla qubits
- Classical correction based on measurement
- Decoding and final measurement in the X-basis to verify state recovery
- Repeating this with the more advanced Shor's Code.

## Notable aspects of this project

- Help for students hoping to learn more on these topics
- Practical use of **Qiskit**
- Simulation of **quantum systems**
- Understanding of **quantum error correction**
- Clear and tested **circuit design**
- Readiness to work on quantum technologies in space and mission-critical systems

## Requirements

- Python 3.8+
- Qiskit

You can install the requirements using:

```bash
pip install -r requirements.txt
```
requirements.txt should include whichever of the requirements.txt corresponds to the notebook being used. Now lets begin with the 'mini-course'

# Quantum Logic Gates

## 1.1 Vector and Matrix Formalism

### 1.1.1 Single Qubits
To begin, the Quantum version of the familiar logic concept of a bit (a state with two options: 'True' and 'False' or '1' and '0' ) can be discussed, needing to take into account that the two possibilities are no longer mutually exclusive:

$$
|0\rangle = \begin{bmatrix} 1 \\
0 \end{bmatrix}, \quad
|1\rangle = \begin{bmatrix} 0 \\
1 \end{bmatrix}, \quad
|+\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\
1 \end{bmatrix}, \quad
|-\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\
-1 \end{bmatrix}, \quad
|+i\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\
i \end{bmatrix}, \quad
|-i\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\
-i \end{bmatrix}
$$

These are the eigenstates of the Pauli matrices:

- Z basis: $$|0\rangle, |1\rangle  $$
- X basis: $$|+\rangle, |-\rangle  $$
- Y basis: $$|+i\rangle, |-i\rangle$$

On the Bloch sphere: $$|+\rangle, |+i\rangle,$$ and $$|0\rangle$$ are on the positive x, y and z axes, while $$\(|-\rangle, |-i\rangle$$ and $$|1\rangle\)$$ are on the corresponding negative axes.

---

### 1.1.2 Two Qubits
One can take the tensor product between a pair of two dimensional column vectors to get a four dimensional vector to represent a two-qubit state:

$$
|00\rangle = \begin{bmatrix} 1 \\
0 \\
0 \\
0 \end{bmatrix}, \quad
|01\rangle = \begin{bmatrix} 0 \\
1 \\
0 \\
0 \end{bmatrix}, \quad
|10\rangle = \begin{bmatrix} 0 \\
0 \\
1 \\
0 \end{bmatrix}, \quad
|11\rangle = \begin{bmatrix} 0 \\
0 \\
0 \\
1 \end{bmatrix}
$$

---

### 1.2 Basic gates for one qubit

#### 1.2.1 Pauli gates
Having 'translated' the logical bit concept to the quantum realm with these vector representations, logic gates can be written as matrices, starting with the Pauli matrices of familiarity to any student of Quantum Mechanics as the infinitesimal generators of the SU(2) symmetry group, which can work as Quantum logic gates. In the Bloch Sphere symbolism, the X, Y and Z gates correspond to half-rotations of a state about the x, y and z axes respectively.

**X-gate (bit flip / NOT):**

$$
X = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix},\quad X|0⟩ = |1⟩,\quad
X|1⟩ = |0⟩$$



**Y-gate (phase + bit flip):**

$$
Y = i \begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix},\quad Y |0⟩ = i|1⟩, \quad Y |1⟩ = -i|0⟩$$


**Z-gate (phase flip):**

$$
Z = \begin{bmatrix} 1 & 0 \\
0 & -1 \end{bmatrix}, \quad
Z |0⟩ = |0⟩, \quad Z |1⟩ = -|1⟩$$

#### 1.2.2 Hadamard gate
This linear combination of the X and Z Pauli gates (equalling $$\frac{1}{\sqrt{2}}(X+Z)$$) can be used to turn the Z eigenstates into the X eigenstates.

$$
H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 
1 & -1 \end{bmatrix}, \quad
H |0⟩ = |+⟩, \quad H |1⟩ = |-⟩
$$

---
## 1.3 CNOT (Controlled-NOT)

$$
\text{CNOT} = \begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{bmatrix}
$$

If the control qubit (first qubit) is 1, the gate flips the target qubit (second qubit), creating entanglement.

---

## 1.4 Toffoli / CCNOT (Controlled-Controlled NOT)

Flips the target qubit only if **both** control qubits are 1.

---

# 2 Quantum Error Correction

## 2.1 Shor Code

- **X-error**: flips $$\(|0\rangle \leftrightarrow |1\rangle\)  $$
- **Z-error**: flips $$\(|+\rangle \leftrightarrow |-\rangle\) $$ 
- **Y-error**: combination of X and Z errors  

### 2.1.1 X-error Identification

Encode \(|\psi\rangle = \alpha|0\rangle + \beta|1\rangle\) as three qubits:

$$
|\psi\rangle = \alpha|000\rangle + \beta|111\rangle
$$

Ancilla qubits detect differences, allowing X-errors to be corrected without measurement.

### 2.1.2 Z-error Identification

Encode $$\(|\psi\rangle = \alpha|+\rangle + \beta|-\rangle\)$$ as three qubits:

$$
|\psi\rangle = \alpha|+++\rangle + \beta|---\rangle
$$

Ancilla qubits detect Z-errors similarly.

### 2.1.3 Combined Protection

To protect against X, Y, Z errors:

1. Encode in $$\(|0\rangle, |1\rangle\)$$ basis (triple qubit).  
2. Switch each qubit to $$\(|+\rangle, |-\rangle\)$$ basis and encode again.  

This creates “double protection” against all single-qubit errors.

# 3 Quantum Classical Hybrid Algorithms

### Quantum Approximation Optimisation Algorithm

QAOA works on optimisation problems (eg: scheduling, postman path challenges, etc.)

It's a hybrid Quantum-Classical system that approximates.

Two Hamiltonians are defined, the cost and mixer ones, which encode the problem and explore the other solutions respectively. An initial state is selected, which can be acted on by unitary operators. The unitary operators chosen here are a succession of alternating operators, exponentiating the choice and mixer Hamiltonians into evolution operators with respect to some evolution parameter, similar to how Hamiltonians are often exponentiated to give time evolution operators. 

$$
e^{-i\alpha H_{\textrm{choice}}}, \quad 
e^{-i\beta H_{\textrm{mixer}}}, \quad 
e^{-i\gamma H_{\textrm{choice}}}, \quad 
e^{-i\delta H_{\textrm{mixer}}}, \ldots
$$

This 'splitting up' of an evolution operator is similar in many ways to Trotterisation:

$$
\lim_{n\rightarrow \infty}\left(e^{-\frac{iAt}{n}}e^{-\frac{iBt}{n}}\right)^n = e^{-i(A+B)t}
$$

Therefore, for large $n$:

$$
e^{-i(A+B)t}\approx \left(e^{-\frac{iAt}{n}}e^{-\frac{iBt}{n}}\right)^n
$$

The QAOA optimisation approach is that if one defines evolution parameters $\beta$ and $\gamma$ and initial quantum state $\ket{\psi}$ then one can use state

$$
\ket{\psi(\alpha,\beta)}=e^{-i\gamma_1 H_{c}} e^{-i\beta_1 H_m}e^{-i\gamma_2 H_c}e^{-i\beta_2 H_m}\dots \ket{\psi}
$$

to find the values of $\beta$ and $\gamma$ that maximise or minimise (depending on the optimisation problem)

$$
E = \bra{\psi(\gamma,\beta)}H_{\textrm{choice}}\ket{\psi(\gamma,\beta)}
$$
