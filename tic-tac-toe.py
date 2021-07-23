# Import statments here
import sys

# Initializing Board, User and CPU Variables
board = []
user = 'X'
cpu = 'O'

# Indices list for row and column for next move, 
# win, draw and loss constant variables
idx_row_col = [0, 0]
WIN = 10
DRAW = 0
LOSS = -10

# Function to Initialize Board
def init_board():
    for row in range(3):
        temp_list = []
        for col in range(3):
            temp_list.append('-')
        board.append(temp_list)

# Function to check if the User or CPU won
def check_win(player):

    # Checking First Row
    if player == board[0][0] == board[0][1] == board[0][2]:
        return True

    # Checking Second Row
    elif player == board[1][0] == board[1][1] == board[1][2]:
        return True

    # Checking Third Row
    elif player == board[2][0] == board[2][1] == board[2][2]:
        return True

    # Checking First Column
    elif player == board[0][0] == board[1][0] == board[2][0]:
        return True

    # Checking Second Column
    elif player == board[0][1] == board[1][1] == board[2][1]:
        return True

    # Checking Third Column
    elif player == board[0][2] == board[1][2] == board[2][2]:
        return True

    # Checking First Diagonal
    elif player == board[0][0] == board[1][1] == board[2][2]:
        return True

    # Checking Second Diagonal
    elif player == board[0][2] == board[1][1] == board[2][0]:
        return True

    else:
        return False

# Function to print the whole board with row and column numbers
def print_board():
    print("------BOARD------")
    print("  0 1 2")
    for count, row in enumerate(board):
        print(count, *row, sep = ' ')

# Function to check if the board is full, by checking all 9 squares
def is_full():
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] != '-':
                count += 1
    return count == 9

# Minimax algorithm
def minimax(flag):

    # Base case, telling the program to stop the recursive call when the 
    # game is over while searching for outcomes or end states
    if check_win(cpu):
        return WIN
    elif check_win(user):
        return LOSS
    elif is_full():
        return DRAW

    # Initializing Variables - Score for each element on the board
    # Minimum and maximum value
    score = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    min_value = 1000
    max_value = -1000

    # Calculating score for all empty squares
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                if flag:
                    board[row][col] = 'O'
                    value = minimax(False)
                else:
                    board[row][col] = 'X'
                    value = minimax(True)
                board[row][col] = '-'
                score[row][col] = value

    # If flag is true (cpu's turn in the algorithm) function finds 
    # square with max score and records indices for next move
    if flag:
        max_value = -1000
        for row in range(3):
            for col in range(3):
                if score[row][col] > max_value and score[row][col]:
                    max_value = score[row][col]
                    idx_row_col[0] = row
                    idx_row_col[1] = col
        return max_value

    # If flag is false (user's turn in the algorithm) function finds 
    # square with min score and records indices for next move
    else:
        min_value = 1000
        for row in range(3):
            for col in range(3):
                if score[row][col] < min_value and score[row][col]:
                    min_value = score[row][col]
                    idx_row_col[0] = row
                    idx_row_col[1] = col
        return min_value

# Function for User's Move
def user_move():
    print_board()
    # Loop that keeps running until the user enters a valid move
    while True:
        print("Enter your move (format: row col): ")
        user_row, user_col = map(int, input().split())
        if board[user_row][user_col] != '-':
            print("Invalid Move!")
            continue
        else:
            board[user_row][user_col] = user
            return

# Function for CPU's Move, utilizing Minimax algorithm
def cpu_move():
    print_board()
    minimax(True)
    # Recalling cpu's move from saved indices for optimal move
    print("CPU Move:", idx_row_col[0], idx_row_col[1])
    board[idx_row_col[0]][idx_row_col[1]] = cpu
    return

# Checking the state of the board
def check_state():
    # Full board and no winner returns a draw
    if is_full():
        print_board()
        print("----DRAW----")
        return True
    # Returning that the User won
    elif check_win(user):
        print_board()
        print("----USER WON----")
        return True
    # Returning that the CPU won
    elif check_win(cpu):
        print_board()
        print("----CPU WON----")
        return True
    else:
        return False

# Function to exit the program
def exit_program():
    print("The program is ending, have a nice day!")
    sys.exit()

# Function for user's choice if they chose help in the interface
def help_choice(choice):
    if choice == "s":
        return
    elif choice == "q":
        exit_program()
    else:
        print("Please enter a valid choice!")
        new_choice = input()
        help_choice(new_choice)


# -------------- MAIN DRIVER CODE --------------

help_text = """-----------HELP-----------
This is a game of Tic-Tac-Toe against a CPU. This game is played
on a 3x3 grid of squares. You are represented by 'X' and the CPU
is represented by 'O'. You and the CPU take turns, by putting your
marks in empty squares. The first player to get 3 of their marks
in a row (up, down, across or diagonally) wins. When all 9 squares
are filled, if no winner is chosen by then, the game results in a tie."""

# Start, help and quit interface
print("Welcome to Tic-Tac-Toe!")
print("Enter 's' to start the game, 'h' for help, or 'q' to quit the program!")

# While loop for user's choice
while True:
    interface_choice = input()

    # Giving the user another choice if they chose help initially
    if interface_choice == "h":
        print(help_text)
        print("Enter 's' to start the game or 'q' to quit the program!")
        h_choice = input()
        help_choice(h_choice)
        break

    # Ending the program if the user chooses q
    elif interface_choice == "q":
        exit_program()

    # Starting the game if the user chooses s
    elif interface_choice == "s":
        break
    
    # Otherwise, telling the user to input a valid choice
    else:
        print("Please enter a valid choice!")

# Initializing the game board
init_board()

# Asking the user if they would like to play first
print("Would you like to play first?")

# Inputting the User's Choice
choice = int(input("User goes first: (1) | CPU goes first: (2) | "))

# Letting the user play first if they choose to
if choice == 1:
    user_move()

# While loop to keep the game running while the board isn't empty
while not check_state():
    cpu_move()
    if check_state():
        break
    user_move()

# Final Game Over Message
print("------GAME OVER------")
exit_program()