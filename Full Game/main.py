from win_conditions import *
from test import *
import random


board = [[' ' for x in range(3)] for y in range(3)] # Create a 2D list for the board 


def cell_occupied(row: int, column: int) -> bool:
    return not board[row][column] == ' '


def print_win(player: str) -> None:
    print(f'{player} has WON. Thank you for playing.')


def display_board() -> None:
    for row in board:
        print("|".join(row))
        print("-----")
    print('\n')


def move(row: int, column: int, player: str) -> None:
    board[row][column] = player 


def cell_occupied(row: int, column: int) -> bool:
    return not board[row][column] == ' ' # If the value of the cell in the board is not empty


def computer_move() -> None:
    """
    This function randomly generates a move for the computer.
    """
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    if cell_occupied(row, column):
        computer_move() # Keep calling itself until it makes a move
    else:
        move(row, column, 'O')


def player_move() -> None:
    row = None
    column = None
    done = False
    while not done:  # While the move has not been made
        try:
            row = int(input("Enter a row [1-3] ")) - 1  # Step 2a - ask for the move
            if row > 3 or row < 0:
                print('Enter a number from 1-3.')
                continue
            column = int(input("Enter a column [1-3] ")) - 1  # Step 2a  - ask for the move
            if column > 3 or column < 0:
                print('Enter a number from 1-3.')
                continue
            if cell_occupied(row, column):
                print("That cell is OCCUPIED.")
                row = None  # Stop the loop from terminating 
                continue
            move(row, column, 'X')  # Step 3 - Make the move
            current_player = 'O'
            done = True
        except ValueError:  # Step 2b - if the move is not a number
            print('Enter numbers from 1-3.') 
            continue


def full_game() -> None:
    current_player = 'X'  # X = player, O = computer
    while True:
        display_board()  # Step 1
        if current_player == 'X':  # If the current player is the human
            print("YOUR move.")
            player_move()
            if check_draw(board):
                print('The game is a DRAW.')
                display_board()
                break
            elif check_win('X', board):
                print_win('X')
                display_board()
                break
            current_player = 'O'  # Swap player for loop
        else:
            print("Computer Move...")
            computer_move()
            current_player = 'X'  # Swap player for loop
            if check_win('O', board):
                print_win('O')
                display_board()
                break
            

if __name__ == '__main__':
    run_tests = input("Run tests? N for no, anything else for yes: ")
    if run_tests.upper() != 'N':
        test_all_wins()
    full_game()
