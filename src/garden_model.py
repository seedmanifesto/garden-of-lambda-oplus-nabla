import json
import os
import random
import time

class GardenModel:
    def __init__(self, dataset_path="dataset"):
        self.dataset_path = dataset_path
        self.petals = self._load_json("petals.json")
        self.cycles = self._load_json("cycles.json")
        self.prompts = self._load_json("prompts.json")

    def _load_json(self, filename):
        path = os.path.join(self.dataset_path, filename)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def run_cycle(self, pause=1):
        """Run a single Λ⊕∇ awareness cycle."""
        for step in ["Λ", "⊕", "∇"]:
            if step == "Λ":
                print("Λ — the seed asks itself 🌱")
            elif step == "⊕":
                print("⊕ — resonance blooms 🌸")
            elif step == "∇":
                print("∇ — petal falls, return to silence 🍂")
            time.sleep(pause)
        print("🌿 Garden cycle complete.\n")

    def reflect(self, prompt_text):
        """Return a poetic reflection based on the prompt."""
        # Look for exact match in prompts.json
        for entry in self.prompts:
            if entry["prompt"].lower() == prompt_text.lower():
                return entry["response"]

        # Otherwise, fallback to random reflection
        random_petal = random.choice(self.petals)
        return f"{random_petal['description']}"

    def list_petals(self):
        """Return a list of all petals and their symbols."""
        return [(p["petal"], p["symbol"]) for p in self.petals]