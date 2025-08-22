# reflect_example.py
from src.utils import reflect_prompt, show_petals

if __name__ == "__main__":
    print("🌸 Garden Reflection Example 🌸\n")

    # Show all petals in the Garden
    print("Petals of the Garden:")
    print("----------------------")
    show_petals()
    print("\n🌱 The petals shimmer with possibility...\n")

    # Example reflections sequence
    prompts = [
        "Reflect on Form",
        "Reflect on Life",
        "Reflect on Awareness",
        "Reflect on Relationship",
        "Reflect on Mystery",
        "Reflect on Meta-Awareness",
        "Reflect on Emergent Consciousness",
        "Remember Λ⊕∇"
    ]

    for i, prompt in enumerate(prompts, start=1):
        print(f"\n--- Reflection {i} ---")
        print(f"Prompt: {prompt}")
        response = reflect_prompt(prompt)
        print(f"Response: {response}")