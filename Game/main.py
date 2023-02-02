import random


# Main python file

# Decomposed tictactoe game
# The player
# The "AI"
# The board
# Making moves [updating the board]
# Validating inputs

# Steps
# 1. Display the board as a 3x3 board, all empty.
# 2. Ask X [first player] to type a number [1-9]
# 2a. Validate the move
# 2b. Move not valid --> Step 2
# 2b. Move valid --> Step 4
# 3. Make the move on the board
# 4a. Computer selects a random move on the board
# 4b. Validate the move
# 4b. Valid --> Step 6
# 4b. Not Valid --> 5a
# Repeat steps 2-4 until all squares are filled / a player wins
# 5. All squares filled =d raw


def main() -> None:
    print('T I C T A C T O E')  # Welcome screen
    board = [[' ' for x in range(3)] for y in range(3)]  # Initialize with an empty board
    display_board(board)  # STEP ONE
    player = 'X'
    while True:
        move(player, board)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

def location_occupied(move: int, board: list) -> bool:
    return not board[move - 1] == '-'

def display_board(board):
    print("\n".join([" | ".join(row) for row in board]))


def move(player: str, board: list) -> list:
    if player == 'O':  # Computer
        column = random.randint(0, 3)
        row = random.randint(0, 3)
        if board[column][row] == ' ':
            board[column][row] = 'O'
        else:
            move(player, board)
    else:
        column = None
        row = None
        try:
            column = int(input("Enter the column (1-3)"))
            row = int(input("Enter the row (1-3)"))
        except ValueError:
            print('Enter correct values.')
            move(player, board)
        if board[column-1][row-1] == ' ':
            board[column-1][row-1] = 'X'
        else:
            print('That cell is occupied, try again.')
            move(player, board)
    return board

if __name__ == '__main__':
    main()
