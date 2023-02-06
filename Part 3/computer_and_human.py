import random

board = [[' ' for x in range(3)] for y in range(3)]


def print_board():
    for row in board:
        print('|'.join(row))
        print('-----')
    print('\n')


def player_move():
    row = int(input("Row [1-3] ")) - 1
    column = int(input("Column [1-3] ")) - 1
    board[row][column] = 'X'


def computer_move():
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    board[row][column] = 'O'


player = 'X'
while True:
    print_board()
    if player == 'X':
        player_move()
        player = 'O'
    else:
        computer_move()
        player = 'X'