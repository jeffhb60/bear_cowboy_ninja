# Bear Cowboy Ninja Game
# This is a command-line game where a user plays against the CPU.
# Similar to "Rock, Paper, Scissors" with three choices: Bear, Cowboy, and Ninja.

# Import random module for CPU choice
import random

# Add function to generate CPU choice
def get_cpu_choice():
    return random.choice(['Bear', 'Cowboy', 'Ninja'])

# Add function to determine the winner based on user and CPU choices
def determine_winner(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        return "Tie"
    elif (user_choice == 'Bear' and cpu_choice == 'Ninja') or \
         (user_choice == 'Cowboy' and cpu_choice == 'Bear') or \
         (user_choice == 'Ninja' and cpu_choice == 'Cowboy'):
        return "User"
    else:
        return "CPU"
