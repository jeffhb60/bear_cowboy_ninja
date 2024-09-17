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

# Implement function to play a single round of the game
def play_round():
    
    # Get user's choice
    user_choice = input("Choose 'Bear', 'Cowboy', or 'Ninja': ").capitalize()

    # Validate user input
    while user_choice not in ['Bear', 'Cowboy', 'Ninja']:
        print("Invalid choice! Please choose 'Bear', 'Cowboy', or 'Ninja'.")
        user_choice = input("Choose 'Bear', 'Cowboy', or 'Ninja': ").capitalize()

    # Get CPU's choice
    cpu_choice = get_cpu_choice()
    print(f"CPU chose: {cpu_choice}")

    # Determine the winner
    winner = determine_winner(user_choice, cpu_choice)
    return winner
