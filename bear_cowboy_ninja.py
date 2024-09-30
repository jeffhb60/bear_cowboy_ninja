import random
import tkinter as tk

from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Bear Cowboy Ninja Game")
root.geometry("500x500")
root.resizable(False, False)  # Disables resizing in both width and height

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


# Modify the play_round function to accept user_choice as an argument
def play_round(user_choice):
    global user_wins, cpu_wins, ties  # Access global score variables

    # Get CPU's choice
    cpu_choice = get_cpu_choice()

    # Determine the winner
    winner = determine_winner(user_choice, cpu_choice)

    # Update labels with choices
    cpu_choice_label.config(text=f"CPU chose: {cpu_choice}")

    # Display the result and update the score
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


# Function to calculate and display final stats upon exiting
def show_final_stats_and_exit():
    total_games = user_wins + cpu_wins + ties
    if total_games == 0:
        win_percentage = 0
    else:
        win_percentage = (user_wins / total_games) * 100

    # Display final stats in a message box
    stats_message = f"Final Stats:\n\nUser Wins: {user_wins}\nCPU Wins: {cpu_wins}\nTies: {ties}\n\nWinning Percentage: {win_percentage:.2f}%"

    # Show the message box for the final stats
    messagebox.showinfo("Game Over", stats_message)

    # Exit the game after the user closes the message box
    root.quit()


# Override the window close button (X) to display final stats
def on_closing():
    show_final_stats_and_exit()

# Set the protocol to capture the window close event (X button)
root.protocol("WM_DELETE_WINDOW", on_closing)

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

bear_button = tk.Button(button_frame, text="Bear", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10,
                        command=lambda: play_round("Bear"))
bear_button.grid(row=0, column=0, padx=10)

cowboy_button = tk.Button(button_frame, text="Cowboy", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10,
                          command=lambda: play_round("Cowboy"))
cowboy_button.grid(row=0, column=1, padx=10)

ninja_button = tk.Button(button_frame, text="Ninja", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT, width=10,
                         command=lambda: play_round("Ninja"))
ninja_button.grid(row=0, column=2, padx=10)

# Score label at the bottom
score_label = tk.Label(root, text="User Wins: 0 | CPU Wins: 0 | Ties: 0", bg=BG_COLOR, fg=TEXT_COLOR, font=SCORE_FONT)
score_label.pack(pady=20)

# Quit button for exiting the game
exit_button = tk.Button(root, text="Exit Game", bg=BTN_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT,
                        command=show_final_stats_and_exit)
exit_button.pack(pady=20)

# Set background color
root.config(bg=BG_COLOR)

# Start the main loop
root.mainloop()
