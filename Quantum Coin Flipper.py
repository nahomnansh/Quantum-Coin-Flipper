"""
Quantum Coin Flipper
--------------------
A tiny CLI game where the coin flip is decided by a real quantum circuit:
a Hadamard gate puts one qubit into an equal superposition of |0> and |1>,
and measuring it collapses it to heads (0) or tails (1) with 50/50 odds.
 
Install:  pip install qiskit qiskit-aer
Run:      python quantum_coin_flip.py
"""
 
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
 
SIM = AerSimulator()
 
 
def build_circuit() -> QuantumCircuit:
    """One qubit, one Hadamard, one measurement."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)           # superposition: (|0> + |1>) / sqrt(2)
    qc.measure(0, 0)  # collapse to 0 or 1
    return qc
 
 
def flip_coin() -> str:
    """Run the circuit once and return 'heads' or 'tails'."""
    compiled = transpile(build_circuit(), SIM)
    counts = SIM.run(compiled, shots=1).result().get_counts()
    bit = next(iter(counts))  # e.g. '0' or '1'
    return "heads" if bit == "0" else "tails"
 
 
def run_many(n: int = 1000) -> dict:
    """Flip n coins at once to show the 50/50 distribution."""
    compiled = transpile(build_circuit(), SIM)
    counts = SIM.run(compiled, shots=n).result().get_counts()
    return {
        "heads": counts.get("0", 0),
        "tails": counts.get("1", 0),
    }
 
 
def play():
    print("=== Quantum Coin Flipper ===")
    print("Commands: [h]eads, [t]ails, [c]ircuit, [s]tats, [q]uit\n")
    wins = losses = 0
 
    while True:
        choice = input("Your call (h/t/c/s/q): ").strip().lower()
 
        if choice in ("q", "quit"):
            break
 
        if choice in ("c", "circuit"):
            print(build_circuit().draw(output="text"))
            continue
 
        if choice in ("s", "stats"):
            result = run_many(1000)
            print(f"1000 quantum flips -> heads: {result['heads']}, "
                  f"tails: {result['tails']}")
            continue
 
        if choice not in ("h", "t", "heads", "tails"):
            print("Please enter h, t, c, s, or q.")
            continue
 
        guess = "heads" if choice.startswith("h") else "tails"
        outcome = flip_coin()
        print(f"The qubit collapsed to: {outcome.upper()}")
 
        if guess == outcome:
            wins += 1
            print("You win!")
        else:
            losses += 1
            print("You lose!")
        print(f"Score: {wins}W - {losses}L\n")
 
    print(f"\nFinal score: {wins}W - {losses}L. Thanks for playing!")
 
 
if __name__ == "__main__":
    play()
