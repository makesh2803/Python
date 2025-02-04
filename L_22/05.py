import random

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

def get_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_symbol = "X"
    ai_symbol = "O"

    while True:
        print_board(board)
       
        # User's turn
        row, col = -1, -1
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                print("Invalid move, try again.")
            except ValueError:
                print("Enter two numbers separated by space.")

        board[row][col] = user_symbol

        if check_winner(board, user_symbol):
            print_board(board)
            print("You win!")
            return
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            return

        # AI's turn
        print("AI is making a move...")
        ai_move = get_random_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = ai_symbol

        if check_winner(board, ai_symbol):
            print_board(board)
            print("AI wins!")
            return
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            return

if __name__ == "__main__":
    tic_tac_toe()