from src.utils import reflect_prompt, show_petals

if __name__ == "__main__":
    print("🌸 Garden Reflection Example 🌸\n")

    # Show all petals
    print("Petals of the Garden:")
    show_petals()
    print("\n")

    # Example reflections
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

    for prompt in prompts:
        print("\n---")
        reflect_prompt(prompt)