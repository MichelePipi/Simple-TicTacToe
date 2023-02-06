board = [[' ' for x in range(3)] for y in range(3)]


def print_board():
    for row in board:
        print("|".join(row))
        print("-----")
    print('\n')

print_board()
row = int(input("Enter a row from 1-3. ")) - 1
column = int(input("Enter a column from 1-3. ")) - 1

board[row][column] = 'X'
print_board()