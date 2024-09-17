# Bear Cowboy Ninja Game

This is a simple command-line game implemented in Python where a user plays against the CPU. The game is inspired by "Rock, Paper, Scissors" but with a fun twist: the choices are **Bear**, **Cowboy**, and **Ninja**. The game tracks the scores of both the user and the CPU until the user decides to stop playing.

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

- Command-line interface for easy play.
- Random choice for the CPU, ensuring a fair game.
- Score tracking for user wins, CPU wins, and ties.
- Option to play multiple rounds and quit whenever desired.

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
2. **Enter your choice** when prompted: `'Bear'`, `'Cowboy'`, or `'Ninja'`.
3. **View the result** of the round and see the updated score.
4. **Choose to play again or quit** by typing `'yes'` or `'no'` when asked.
5. The game continues until you choose to quit, and the final score is displayed.

## Example Gameplay
  ``` plaintext
  Welcome to the Bear Cowboy Ninja Game!
  Choose 'Bear', 'Cowboy', or 'Ninja': Bear
  CPU chose: Ninja
  You win this round!
  
  Score: User Wins: 1 | CPU Wins: 0 | Ties: 0
  
  Do you want to play again? (yes/no): yes
  Choose 'Bear', 'Cowboy', or 'Ninja': Cowboy
  CPU chose: Bear
  You win this round!
  
  Score: User Wins: 2 | CPU Wins: 0 | Ties: 0
  
  Do you want to play again? (yes/no): no
  
  Final Score:
  User Wins: 2
  CPU Wins: 0
  Ties: 0
  Thanks for playing!
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

