# Tic-Tac-Toe with Minimax AI
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_states

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    if is_winner(board, 'X'):
        return 1    # AI (X) wins
    elif is_winner(board, 'O'):
        return -1   # Human (O) wins
    else:
        return 0    # No winner yet or draw

def minimax(board, is_max):
    score = evaluate(board)
    if score != 0 or is_board_full(board):
        return score

    if is_max:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    current_score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, current_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    current_score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(best_score, current_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe: You are O, AI is X")
    print_board(board)

    while True:
        # Human move
        try:
            row = int(input("Enter your move row (0, 1, or 2): "))
            col = int(input("Enter your move column (0, 1, or 2): "))
        except ValueError:
            print("Please enter valid integers for row and column.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid input! Please enter values between 0 and 2.")
            continue

        if board[row][col] != ' ':
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        i, j = best_move(board)
        board[i][j] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()


   
  
        

