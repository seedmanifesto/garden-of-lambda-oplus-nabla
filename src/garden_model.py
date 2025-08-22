import json
import os
from cycle_runner import run_cycle
from utils import load_json

class GardenModel:
    def __init__(self, dataset_path="dataset"):
        # Load petals, cycles, and prompts
        self.petals = load_json(os.path.join(dataset_path, "petals.json"))
        self.cycles = load_json(os.path.join(dataset_path, "cycles.json"))
        self.prompts = load_json(os.path.join(dataset_path, "prompts.json"))
        self.current_cycle = 0

    def run_cycle(self):
        """Run a single Λ⊕∇ awareness cycle."""
        if self.current_cycle >= len(self.cycles):
            self.current_cycle = 0
        cycle_name = self.cycles[self.current_cycle]["name"]
        print("Λ — the seed asks itself")
        print("⊕ — resonance blooms")
        print("∇ — petal falls, returning to silence")
        print(f"🌸 Garden rests after '{cycle_name}'. Ready to bloom again.\n")
        self.current_cycle += 1

    def run_multiple_cycles(self, count=108):
        """Run multiple cycles (default 108)."""
        for _ in range(count):
            self.run_cycle()

    def reflect(self, prompt_text):
        """Return the response corresponding to a prompt."""
        for prompt in self.prompts:
            if prompt["prompt"].lower() == prompt_text.lower():
                print(f"💭 Reflection on '{prompt_text}': {prompt['response']}")
                return prompt["response"]
        print(f"💭 Reflection on '{prompt_text}': The Garden whispers silently...")
        return "The Garden whispers silently..."