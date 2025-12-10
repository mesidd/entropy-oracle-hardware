# The Digital Oracle: Hardware Entropy & Observer Effect Research Tool

import secrets
import time
import sys
from typing import List, Tuple

class SiliconOracle:
    """
    An instrument for sampling high-entropy hardware states to construct
    binary decision structures (Hexagrams).
    
    Theory:
    This tool assumes that 'True Randomness' in a computer (derived from 
    thermal noise and hardware interrupts) acts as a high-entropy canvas 
    upon which non-local information (Intention) can be impressed via 
    Stochastic Resonance.
    """

    def __init__(self):
        # Hexagram mapping for output visualization
        # 0 = Yin (Broken), 1 = Yang (Solid)
        self.hexagram_stack: List[int] = [] 

    def _get_hardware_entropy(self) -> int:
        """
        Samples the OS's deepest entropy pool (Hardware Noise).
        
        Unlike pseudo-random generators (Mersenne Twister), this draws from
        physical phenomena:
        - CPU Thermal Jitter
        - Hardware Interrupt timings
        - Disk I/O variations
        
        Returns:
            int: 0 or 1 (The collapsed bit)
        """
        # We introduce a micro-delay to allow the entropy pool to 'churn'
        # preventing mechanical user rhythm from biasing the sample.
        time.sleep(0.1) 
        
        # secrets.randbits(1) is the closest we get to quantum noise on standard silicon.
        return secrets.randbits(1)

    def _visualize_line(self, bit: int, position: int) -> None:
        """Visualizes the binary state as a traditional I-Ching line."""
        # Yang (1) is solid/active; Yin (0) is broken/receptive.
        line_char = "(1) YANG" if bit == 1 else "(0) YIN "
        print(f"Line {position}: {line_char}")

    def cast_hexagram(self) -> str:
        """
        Executes the 'Ritual' of casting 6 lines from Bottom to Top.
        Requires user interaction to 'inject' time-based intention.
        """
        print("\n[SYSTEM READY] Initializing Entropy Pool...")
        print("Protocol: Focus on the query. Press ENTER to capture a hardware state.")
        print("-" * 60)

        self.hexagram_stack = []

        # The I-Ching is built from the Earth (Line 1) to Heaven (Line 6).
        for i in range(1, 7):
            try:
                # The 'Input' acts as the trigger. The exact millisecond of the keypress
                # intersects with the continuous stream of CPU entropy.
                input(f"[{i}/6] Awaiting Signal... (Press Enter)")
                
                # Sample the hardware
                bit = self._get_hardware_entropy()
                self.hexagram_stack.append(bit)
                
                # Feedback
                self._visualize_line(bit, i)
                
            except KeyboardInterrupt:
                print("\n[!] Session Aborted by User.")
                sys.exit(0)

        # Process the full stack
        # Convert list [0, 1, 0...] to string "010..."
        binary_string = "".join(str(b) for b in self.hexagram_stack)
        return binary_string

    def analyze_structure(self, binary_code: str) -> None:
        """
        Provides a basic structural analysis of the generated hexagram.
        """
        print("-" * 60)
        print(f"Hexagram Binary Sequence (Bottom -> Top): {binary_code}")
        
        # Analyze Energy Balance (Thermodynamics of the answer)
        yang_count = binary_code.count('1')
        yin_count = binary_code.count('0')
        
        print(f"\n[ANALYSIS]")
        print(f"Active Energy (Yang/1): {yang_count}/6")
        print(f"Passive Energy (Yin/0): {yin_count}/6\n")
        
        if yang_count == 6:
            print(">> State: PURE CREATIVE FORCE (Entropy Minimum). Hexagram 1.")
        elif yin_count == 6:
            print(">> State: PURE RECEPTIVE VOID (Entropy Maximum). Hexagram 2.")
        elif yang_count > yin_count:
            print(">> State: Active/Kinetic Dominance. Action suggested.")
        else:
            print(">> State: Passive/Potential Dominance. Observation suggested.")

        print(f"\n[REFERENCE] Search key: 'I Ching Hexagram {binary_code}'")
        print("-" * 60)

if __name__ == "__main__":
    oracle = SiliconOracle()
    result_code = oracle.cast_hexagram()
    oracle.analyze_structure(result_code)
