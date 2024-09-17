# Bear Cowboy Ninja Game
# This is a command-line game where a user plays against the CPU.
# Similar to "Rock, Paper, Scissors" with three choices: Bear, Cowboy, and Ninja.

# Import random module for CPU choice
import random

# Add function to generate CPU choice
def get_cpu_choice():
    """
        Randomly selects the CPU's choice from 'Bear', 'Cowboy', or 'Ninja'.
    
        Returns:
            str: The CPU's choice ('Bear', 'Cowboy', or 'Ninja').
    """
    return random.choice(['Bear', 'Cowboy', 'Ninja'])

# Add function to determine the winner based on user and CPU choices
def determine_winner(user_choice, cpu_choice):
       """
            Determines the winner based on user and CPU choices.
            
            Args:
                user_choice (str): The user's choice ('Bear', 'Cowboy', or 'Ninja').
                cpu_choice (str): The CPU's choice ('Bear', 'Cowboy', or 'Ninja').
            
            Returns:
                str: The winner of the round ('User', 'CPU', or 'Tie').
    """
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
   """
        Plays one round of the game, gets user input, CPU's choice, and determines the winner.
        
        Returns:
            str: The winner of the round ('User', 'CPU', or 'Tie').
    """    
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

# Add main game loop to manage rounds and track scores
def main():
    """
        Main function to run the game loop. Tracks scores and asks the user if they want to play again.
    """
    # Initialize scores
    user_wins = 0
    cpu_wins = 0
    ties = 0

    print("Welcome to the Bear Cowboy Ninja Game!")  # Welcome message
    
    while True:
        # Play a round and determine the winner
        winner = play_round()

        # Update scores based on the winner
        if winner == "User":
            print("You win this round!")
            user_wins += 1
        elif winner == "CPU":
            print("CPU wins this round!")
            cpu_wins += 1
        else:
            print("This round is a tie!")
            ties += 1

        # Display the current score
        print(f"\nScore: User Wins: {user_wins} | CPU Wins: {cpu_wins} | Ties: {ties}\n")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Display the final score when the user decides to stop playing
    print("\nFinal Score:")
    print(f"User Wins: {user_wins}")
    print(f"CPU Wins: {cpu_wins}")
    print(f"Ties: {ties}")
    print("Thanks for playing!")

# Add entry point to run the game
if __name__ == "__main__":
    main()
