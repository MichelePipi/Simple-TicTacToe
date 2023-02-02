from lib import *

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
# 2b. Move valid --> Step 3
# 3a. Make the move on the board
# 3b. Win/Draw/Impossible? --> END GAME
# 4a. Computer selects a random move on the board
# 4b. Validate the move
# 4b. Valid --> Step 6
# 4b. Not Valid --> 5a
# 4c. Win/Draw/Impossible? --> END GAME
# Repeat steps 2-4 until an outcome occurs


def main() -> None:
    board = [[' ' for x in range(3)] for y in range(3)]  # init board
    current_player = 'X'  # X = player, O = computer
    while True:
        display_board(board)  # Step 1
        if current_player == 'X':
            row = None
            column = None
            while row is None and column is None:
                try:
                    row = int(input("Enter a column [1-3] ")) - 1  # Step 2a
                    column = int(input("Enter a row [1-3]")) - 1  # Step 2a
                except ValueError:  # Step 2b
                    print('Enter a value from 1-9.')
                    continue
                if cell_occupied(row, column, board):
                    print("That cell is OCCUPIED.")
                    continue
                board[row][column] = 'X'  # Step 3

if __name__ == '__main__':
    main()
