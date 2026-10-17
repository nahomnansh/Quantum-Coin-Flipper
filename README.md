# 🪙 Quantum Coin Flipper

A CLI coin-flipping game powered by Qiskit and quantum superposition.

## 📌 Overview
Unlike classical pseudorandom number generators (PRNGs), this program utilizes true quantum randomness. It places a single qubit into an equal superposition state using a **Hadamard gate** ($\frac{\vert{}0\rangle + \vert{}1\rangle}{\sqrt{2}}$) and measures it to collapse the state to either `0` (Heads) or `1` (Tails) with true 50/50 probability.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Qiskit & Qiskit Aer

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/quantum-coin-flipper.git](https://github.com/YOUR-USERNAME/quantum-coin-flipper.git)
   cd quantum-coin-flipper
