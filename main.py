import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move():
    while True:
        try:
            move = input("Enter your move (row and column, e.g., '0 0'): ")
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid move. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers.")

def get_ai_move(board):
    # Simple AI: Randomly choose an empty cell
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = get_player_move()
        else:
            row, col = get_ai_move(board)
            print(f"Player O chooses: {row} {col}")

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
