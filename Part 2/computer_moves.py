import random

board = [[' ' for x in range(3)] for y in range(3)]


def print_board():
    for row in board:
        print('|'.join(row))
        print('-----')
    print('\n')


def computer_move():
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    board[row][column] = 'O'


while True:
    print_board()
    move = input("Press ENTER to make the computer move.")
    computer_move()