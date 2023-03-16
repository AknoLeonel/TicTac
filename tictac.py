from random import randrange

def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def get_user_move(board):
    valid_move = False
    while not valid_move:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move)
            if move in range(1, 10):
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == str(move):
                    valid_move = True
                else:
                    print("That key is already occupied.")
            else:
                print("Move must be a number between 1 and 9.")
        else:
            print("Move must be a number between 1 and 9.")
    return row, col

def get_computer_move(board):
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] != "X" and board[row][col] != "O":
            break
    return row, col

def check_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != str(i*3+1):
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != str(i+1):
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "1":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "3":
        return board[0][2]
    for row in board:
        for square in row:
            if square.isdigit():
                return None
    return "Tie"

def play_game():
    board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
    print_board(board)
    while True:
        user_row, user_col = get_user_move(board)
        board[user_row][user_col] = "O"
        print_board(board)
        result = check_game_over(board)
        if result is not None:
            if result == "Old Lady":
                print("Old Lady")
            else:
                print("YOU WIN SIIIIUUU")
            return
        computer_row, computer_col = get_computer_move(board)
        board[computer_row][computer_col] = "X"
        print_board(board)
        result = check_game_over(board)
        if result is not None:
            if result == "Old Lady":
                print("Old Lady!")
            else:
                print("Pc wins!")
            return

play_game()







