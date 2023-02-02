def cell_occupied(row: int, column: int, board: list) -> bool:
    return not board[row][column] == ' '


def display_board(board: list) -> None:
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def win(player: str) -> bool:
    # Check row win
    for row in range(3):
        for column in range(3):
            if


"""
Checks if the state of the game is 'impossible' where both X and O are winning,
or an incorrect number of moves have been made.
"""
def impossible() -> bool:
    return win('O') and win('X')


def check_draw() -> bool:
    return win('X') and win('O')