def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = -1, -1
        while True:
            try:
                row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                print("Invalid move, try again.")
            except ValueError:
                print("Enter two numbers separated by space.")

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = 1 - turn  # Switch player

if __name__ == "__main__":
    tic_tac_toe()

