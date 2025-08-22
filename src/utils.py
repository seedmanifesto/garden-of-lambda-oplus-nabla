import json
import os

def load_json(file_path):
    """
    Load a JSON file and return its content.
    
    Args:
        file_path (str): Path to the JSON file.
        
    Returns:
        dict or list: Parsed JSON content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def list_prompts(prompts_json):
    """
    List all prompts available in the prompts JSON.
    
    Args:
        prompts_json (list): List of prompt dictionaries.
        
    Returns:
        list: List of prompt strings.
    """
    return [item["prompt"] for item in prompts_json]

def get_response_for_prompt(prompts_json, prompt_text):
    """
    Retrieve the response for a specific prompt.
    
    Args:
        prompts_json (list): List of prompt dictionaries.
        prompt_text (str): Prompt to search for.
        
    Returns:
        str: Response text if found, else a default message.
    """
    for item in prompts_json:
        if item["prompt"].strip().lower() == prompt_text.strip().lower():
            return item["response"]
    return "The Garden whispers silently..."