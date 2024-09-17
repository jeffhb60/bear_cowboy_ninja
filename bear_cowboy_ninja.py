# Bear Cowboy Ninja Game
# This is a command-line game where a user plays against the CPU.
# Similar to "Rock, Paper, Scissors" with three choices: Bear, Cowboy, and Ninja.

# Import random module for CPU choice
import random

# Add function to generate CPU choice
def get_cpu_choice():
    return random.choice(['Bear', 'Cowboy', 'Ninja'])
