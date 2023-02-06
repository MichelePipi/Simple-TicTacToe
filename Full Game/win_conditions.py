def check_column_win(player: str, board: list) -> bool:
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False


def check_row_win(player: str, board: list) -> bool:
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_diagonal_win(player: str, board: list) -> bool:
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def check_win(player: str, board: list) -> bool:
    """
    This function first checks if the player has won in any possibility.
    """
    return check_row_win(player, board) or check_column_win(player, board) or check_diagonal_win(player, board)

"""
Checks if the game is a draw.
"""
def check_draw(board: list) -> bool:
    return check_win('O', board) and check_win('X', board)
   