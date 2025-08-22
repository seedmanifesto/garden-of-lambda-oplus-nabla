from garden_model import GardenModel

def run_garden_cycles(n=108, pause=1):
    """
    Run n sequential Λ⊕∇ awareness cycles (default 108).
    """
    garden = GardenModel()
    for i in range(n):
        print(f"--- Cycle {i + 1} ---")
        garden.run_cycle(pause=pause)

if __name__ == "__main__":
    run_garden_cycles()  # runs 108 cycles by default