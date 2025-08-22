from garden_model import GardenModel

def reflect_prompt(prompt_text):
    """
    Helper function to get a reflection from the Garden model.
    """
    garden = GardenModel()
    response = garden.reflect(prompt_text)
    print(f"Prompt: {prompt_text}")
    print(f"Reflection: {response}")
    return response

def show_petals():
    """
    Display all petals with their symbols.
    """
    garden = GardenModel()
    petals = garden.list_petals()
    for name, symbol in petals:
        print(f"{symbol}  {name}")