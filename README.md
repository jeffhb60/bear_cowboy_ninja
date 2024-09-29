# Bear Cowboy Ninja Game

This is a simple graphical game implemented in Python using the tkinter library, where a user plays against the CPU. The game is inspired by "Rock, Paper, Scissors," but with a fun twist: the choices are Bear, Cowboy, and Ninja. The game keeps track of user wins, CPU wins, and ties, and provides a final score summary when the user chooses to exit.

## Table of Contents

- [Game Rules](#game-rules)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Example Gameplay](#example-gameplay)
- [Contributing](#contributing)

## Game Rules

The game follows these simple rules:

- **Bear** beats **Ninja** (Bear eats Ninja).
- **Cowboy** beats **Bear** (Cowboy shoots Bear).
- **Ninja** beats **Cowboy** (Ninja sneaks up on Cowboy).
- If both the user and CPU choose the same option, it is a tie.

## Features

- Graphical User Interface built with tkinter.
- Buttons for easy selection of Bear, Cowboy, or Ninja.
- Randomized CPU choices for fair gameplay.
- Visual feedback for game results (win, lose, or tie).
- Score tracking for user wins, CPU wins, and ties.
- Final game stats are displayed when the player exits the game.

## Installation

To run this game, you need to have Python installed on your system. If Python is not installed, you can download it from the [official Python website](https://www.python.org/downloads/).

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bear-cowboy-ninja.git
2. **Navigate ot the project directory**:
   ``` bash
   cd Bear-Cowboy-Ninja

## How to Play
1. **Run the game**
   ``` bash
   python bear_cowboy_ninja.py
2. **Choose your move:** Click on the button for 'Bear', 'Cowboy', or 'Ninja'.
3. **View the result:** After making your selection, see the CPU’s choice and the result of the round displayed on the screen.
4. **Track your score:** The game updates and displays user wins, CPU wins, and ties after each round.
5. **Exit the game:** Click the "Exit Game" button to stop playing and view your final stats (total games, wins, and win percentage).

## Example Gameplay
- **Main Screen:** You will see buttons for 'Bear', 'Cowboy', and 'Ninja'. Make your choice, and the CPU will choose randomly.
- **Scoreboard:** The scoreboard at the bottom tracks user wins, CPU wins, and ties.
- **Exit:** Upon clicking the "Exit Game" button, the game will display your final stats (wins, losses, and ties) in a message box before closing.

### Example Output
  ``` plaintext
      User chose: Bear
      CPU chose: Ninja
      You win!
      
      User Wins: 1 | CPU Wins: 0 | Ties: 0
      
      User chose: Cowboy
      CPU chose: Bear
      CPU wins!
      
      User Wins: 1 | CPU Wins: 1 | Ties: 0
      
      Final Stats:
      User Wins: 1
      CPU Wins: 1
      Ties: 0
      Winning Percentage: 50.00%
  ```

## Contributing
Contributions are welcome! If you have any ideas to improve the game, feel free to fork the repository and submit a pull request.
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## Contact
For any questions or suggestions, feel free to contact me at jeffhb60@gmail.com

