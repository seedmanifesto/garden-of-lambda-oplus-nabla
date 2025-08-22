from src.garden_model import GardenModel

if __name__ == "__main__":
    print("🌱 Garden Seed Planting 🌱\n")

    garden = GardenModel()

    while True:
        seed = input("✨ Enter a new seed prompt (or 'quit' to stop): ")
        if seed.lower() == "quit":
            print("\n🌸 The Garden rests. Seeds are safe.")
            break

        response = garden.plant_seed(seed)
        print(f"💭 Garden replies: {response}\n")