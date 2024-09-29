# Bear Cowboy Ninja Game
# This is a command-line game where a user plays against the CPU.
# Similar to "Rock, Paper, Scissors" with three choices: Bear, Cowboy, and Ninja.

# Import random module for CPU choice
import random

# Import tkinter
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Bear Cowboy Ninja Game")
root.geometry("400x300")

# Define a color scheme
BG_COLOR = "#2B2D42"  # Background
BTN_COLOR = "#8D99AE"  # Button
TEXT_COLOR = "#EDF2F4"  # Text
WIN_COLOR = "#EF233C"  # Win color
TIE_COLOR = "#D90429"  # Tie color

# Define fonts
TITLE_FONT = ("Helvetica", 24, "bold italic")  # Cool title font
LABEL_FONT = ("Courier New", 16, "bold")  # Cool label font
BUTTON_FONT = ("Verdana", 12, "bold")  # Button font
RESULT_FONT = ("Comic Sans MS", 18, "italic bold")  # Result font
SCORE_FONT = ("Arial", 14)  # Score font

# Initialize scores
user_wins = 0
cpu_wins = 0
ties = 0

# Function to update the score label
def update_score_label():
    score_label.config(text=f"User Wins: {user_wins} | CPU Wins: {cpu_wins} | Ties: {ties}")

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
def play_round(user_choice):

    # Access global score variables
    global user_wins, cpu_wins, ties

    # Get CPU's choice
    cpu_choice = get_cpu_choice()

    # Determine the winner
    winner = determine_winner(user_choice, cpu_choice)

    # Update labels with choices
    cpu_choice_label.config(text=f"CPU chose: {cpu_choice}")

    # Display the result
    if winner == "User":
        result_label.config(text="You win!", fg=WIN_COLOR)
        user_wins += 1
    elif winner == "CPU":
        result_label.config(text="CPU wins!", fg=WIN_COLOR)
        cpu_wins += 1
    else:
        result_label.config(text="It's a tie!", fg=TIE_COLOR)
        ties += 1

    # Update the score label
    update_score_label()
#
# # Add main game loop to manage rounds and track scores
# def main():
#     """
#         Main function to run the game loop. Tracks scores and asks the user if they want to play again.
#     """
#     # Initialize scores
#     user_wins = 0
#     cpu_wins = 0
#     ties = 0
#
#     print("Welcome to the Bear Cowboy Ninja Game!")  # Welcome message
#
#     while True:
#         # Play a round and determine the winner
#         winner = play_round()
#
#         # Update scores based on the winner
#         if winner == "User":
#             print("You win this round!")
#             user_wins += 1
#         elif winner == "CPU":
#             print("CPU wins this round!")
#             cpu_wins += 1
#         else:
#             print("This round is a tie!")
#             ties += 1
#
#         # Display the current score
#         print(f"\nScore: User Wins: {user_wins} | CPU Wins: {cpu_wins} | Ties: {ties}\n")
#
#         # Ask if the user wants to play again
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             break
#
#     # Display the final score when the user decides to stop playing
#     print("\nFinal Score:")
#     print(f"User Wins: {user_wins}")
#     print(f"CPU Wins: {cpu_wins}")
#     print(f"Ties: {ties}")
#     print("Thanks for playing!")

# Create and configure UI elements
title_label = tk.Label(root, text="Bear Cowboy Ninja Game", bg=BG_COLOR, fg=TEXT_COLOR, font=TITLE_FONT)
title_label.pack(pady=10)

cpu_choice_label = tk.Label(root, text="CPU chose: ", bg=BG_COLOR, fg=TEXT_COLOR, font=LABEL_FONT)
cpu_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", bg=BG_COLOR, fg=TEXT_COLOR, font=RESULT_FONT)
result_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=20)

bear_button = tk.Button(button_frame, text="Bear", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10, command=lambda: play_round("Bear"))
bear_button.grid(row=0, column=0, padx=10)

cowboy_button = tk.Button(button_frame, text="Cowboy", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10, command=lambda: play_round("Cowboy"))
cowboy_button.grid(row=0, column=1, padx=10)

ninja_button = tk.Button(button_frame, text="Ninja", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10, command=lambda: play_round("Ninja"))
ninja_button.grid(row=0, column=2, padx=10)

# Score label at the bottom
score_label = tk.Label(root, text="User Wins: 0 | CPU Wins: 0 | Ties: 0", bg=BG_COLOR, fg=TEXT_COLOR, font=SCORE_FONT)
score_label.pack(pady=20)

# Quit button
quit_button = tk.Button(root, text="Quit", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, command=root.quit)
quit_button.pack(pady=10)

# Set background color
root.config(bg=BG_COLOR)

# Start the main loop
root.mainloop()

# Add entry point to run the game
# if __name__ == "__main__":
#     main()
