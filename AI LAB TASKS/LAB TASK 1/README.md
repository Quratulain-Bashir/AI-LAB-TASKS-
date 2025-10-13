# Quratulain 
## roll no: 156 
### section : bsai 3c
*******************************************


## Tic-Tac-Toe CLI Game

This Python script implements a simple command-line Tic-Tac-Toe game for two players.

### How It Works

    - The game board is represented by a list of positions (0-8).
    - Players take turns entering the position where they want to place their mark ('X' or 'O').
    - The board is displayed after each move.
    - The game checks for a winner after every move using standard Tic-Tac-Toe winning patterns (rows, columns, diagonals).
    - If all positions are filled and there is no winner, the game ends in a draw.
    - The game can be aborted with `Ctrl+C` or by sending an EOF signal.

### How to Play

    1. Run the script in a terminal.
    2. Enter the position number (0-8) when prompted.
    3. The game will indicate if a position is already taken or if the input is invalid.
    4. The game announces the winner or a draw at the end.
