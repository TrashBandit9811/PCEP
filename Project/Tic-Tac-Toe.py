# This is a program that pretends to play Tic-Tac-Toe with you.
import random

# The computer plays as 'X' and you play as 'O'.
# The first move belongs to the computer, putting an 'X' in the center of the board.
# All the squares are numbered from 1 to 9, starting from the top left corner.
# The user inputs the number of the square where they want to place their 'O'.

def printboard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

board = [['1','2','3'],['4','5','6'],['7','8','9']]
board[1][1] = 'X'  # Computer's first move
print("Welcome to Tic-Tac-Toe!")
print("First move is made by the computer (X) in the center square.")
printboard(board)

while True:
    # User's turn
    while True:
        try:
            move = int(input("Enter the number of the square where you want to place your 'O': "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] in ['X', 'O']:
                print("Square already taken. Choose another square.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    printboard(board)

    # Check for user win
    for i in range(3):
        if all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            print("Congratulations! You win!")
            exit()

    if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        print("Congratulations! You win!")
        exit()

    # Computer's turn
    available_moves = [str(i) for i in range(1, 10) if board[(i - 1) // 3][(i - 1) % 3] not in ['X', 'O']]
    if not available_moves:
        print("It's a draw!")
        exit()
    
    move = random.choice(available_moves)
    row, col = divmod(int(move) - 1, 3)
    board[row][col] = 'X'
    print(f"Computer places 'X' in square {move}.")
    
    printboard(board)

    # Check for computer win
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            print("Computer wins! Better luck next time.")
            exit()

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        print("Computer wins! Better luck next time.")
        exit()