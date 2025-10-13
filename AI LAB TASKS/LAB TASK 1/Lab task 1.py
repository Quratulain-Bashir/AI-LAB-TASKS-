# Simple CLI Tic-Tac-Toe game (improved)

positions = [str(i) for i in range(9)]

winning_patterns = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def show_board():
    print()
    print(f" {positions[0]} | {positions[1]} | {positions[2]} ")
    print("---+---+---")
    print(f" {positions[3]} | {positions[4]} | {positions[5]} ")
    print("---+---+---")
    print(f" {positions[6]} | {positions[7]} | {positions[8]} ")
    print()

def check_winner():
    for a,b,c in winning_patterns:
        if positions[a] == positions[b] == positions[c]:
            return positions[a]  # 'X' or 'O'
    return None

def play():
    players = ["X", "O"]
    move_count = 0

    try:
        while move_count < 9:
            current = players[move_count % 2]
            show_board()
            prompt = f"Player {current} - enter position (0-8): "
            while True:
                try:
                    move = int(input(prompt).strip())
                except ValueError:
                    print("Please enter a number between 0 and 8.")
                    continue
                if move < 0 or move > 8:
                    print("Position must be between 0 and 8.")
                    continue
                if positions[move] in ("X", "O"):
                    print("That position is already taken. Choose another.")
                    continue
                break

            positions[move] = current
            move_count += 1

            winner = check_winner()
            if winner:
                show_board()
                print(f"Player {winner} wins the game!")
                return

        show_board()
        print("Game Draw!")
    except (KeyboardInterrupt, EOFError):
        print("\nGame aborted.")

if __name__ == "__main__":
    play()
