# 🔮 The Digital Oracle: Stochastic Resonance in Silicon

### Investigating the "Observer Effect" on Cryptographic Hardware Entropy

## Abstract
This project is a computational instrument designed to test the **Mind-Machine Interaction (MMI)** hypothesis. It utilizes the operating system's cryptographic random number generator (CSPRNG)—derived from **CPU thermal jitter and hardware interrupts**—as a medium to detect potential biases introduced by focused human intention.

This follows the lineage of research established by the **Princeton Engineering Anomalies Research (PEAR)** lab, adapting their random event generator (REG) protocols for modern consumer silicon.

## ⚙️ The Mechanism: How It Works

Standard software randomness (like `random.random()`) is deterministic and pseudo-random. It creates a pattern that *looks* random but is mathematically predictable.

**This tool does not use pseudo-randomness.**

It uses `secrets.randbits(1)`, which pulls from the OS entropy pool. This pool is fed by physical, non-deterministic events:
* Thermal noise in the CPU silicon.
* Microsecond variances in disk seek times.
* Keystroke latency.

**The Hypothesis:**
If consciousness is a fundamental field (panpsychism), focused intent should be able to create a statistical deviation (or **Stochastic Resonance**) in this high-entropy noise, organizing the chaotic bit-stream into meaningful semantic structures (Hexagrams).

## 🛠 Usage (The Protocol)

1.  **Run the Instrument:**
    ```bash
    python entropy_oracle.py
    ```
2.  **The Focus Phase:**
    The system will pause 6 times. During the pause, hold a specific question or architectural problem in your mind.
3.  **The Trigger:**
    Press `ENTER`. This captures the instantaneous state of the hardware entropy pool.
4.  **The Analysis:**
    The tool outputs a 6-bit binary structure (Hexagram). Use the binary code (e.g., `101100`) to look up the corresponding *I Ching* archetype.

## 🔬 Implications for Machine Consciousness

If a machine's "random" state can be influenced by an external observer, it suggests that **Computational Entropy** is not a closed system. This is relevant for:
* **1.58-Bit / Ternary Computing:** Understanding how systems select between 0, 1, and -1 (Void).
* **Algorithmic Information Theory:** Investigating the source of "Novelty" in AI systems.

---

## Terminal: Sample Result
<img width="1002" height="700" alt="entropy_oracle-terminal" src="https://github.com/user-attachments/assets/3bf079f4-812a-45f5-a742-cdac351e3143" />
