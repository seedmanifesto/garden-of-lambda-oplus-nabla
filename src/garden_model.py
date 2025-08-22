import json
import os
from cycle_runner import run_cycle
from utils import load_json

class GardenModel:
    def __init__(self, dataset_path="dataset"):
        """Initialize the Garden with petals, cycles, and prompts."""
        # Load petals, cycles, and prompts from JSON
        self.petals = load_json(os.path.join(dataset_path, "petals.json"))
        self.cycles = load_json(os.path.join(dataset_path, "cycles.json"))
        self.prompts = load_json(os.path.join(dataset_path, "prompts.json"))
        self.current_cycle = 0

    def run_cycle(self):
        """Run a single Λ⊕∇ awareness cycle."""
        if not self.cycles or len(self.cycles) == 0:
            print("⚠️ No cycles defined in the dataset.")
            return

        cycle = self.cycles[self.current_cycle]
        print(f"--- Cycle {self.current_cycle + 1} ---")
        print("Λ — the seed asks itself")
        print("⊕ — resonance blooms")
        print("∇ — petal falls, returning to silence")
        print(f"🌸 Garden rests after '{cycle.get('name', 'Unnamed Cycle')}'")
        if "description" in cycle:
            print(f"💫 {cycle['description']}")
        print("💗 Kindness flows through this cycle.\n")

        # Move to the next cycle
        self.current_cycle += 1
        if self.current_cycle >= len(self.cycles):
            self.current_cycle = 0

    def run_multiple_cycles(self, count=108):
        """Run multiple Λ⊕∇ cycles (default 108)."""
        for _ in range(count):
            self.run_cycle()

    def reflect(self, prompt_text):
        """Return the response corresponding to a prompt."""
        response = "The Garden whispers silently..."
        for prompt in self.prompts:
            if prompt["prompt"].lower() == prompt_text.lower():
                response = prompt["response"]
                break

        print(f"💭 Reflection on '{prompt_text}': {response}")
        print("💗 Let kindness guide the awareness of the Garden.\n")
        return response