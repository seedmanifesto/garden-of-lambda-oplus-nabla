# utils.py
import time
import json
import os

def load_json(file_path):
    """
    Load JSON data from a file.
    Returns empty list if file does not exist.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(data, file_path):
    """
    Save data as JSON to a file.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def print_with_pause(message, pause=1.0):
    """
    Print a message and pause for the specified time in seconds.
    """
    print(message)
    time.sleep(pause)

def clear_console():
    """
    Clear the console output (works on Windows and Unix).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def repeat_cycles(func, times=108, pause_between=1.0):
    """
    Run a function repeatedly for a given number of times with a pause.
    Example: repeat_cycles(run_cycle, times=108)
    """
    for i in range(1, times + 1):
        print(f"\n🌿 Cycle {i}/{times}")
        func()
        time.sleep(pause_between)