from win_conditions import *


def test_win_conditions():
    # Test horizontal win
    board = [['X', 'X', 'X'],
             ['O', 'O', ' '],
             [' ', ' ', ' ']]
    assert check_win('X', board) == True

    board = [['O', 'O', 'O'],
             ['X', 'X', ' '],
             [' ', ' ', ' ']]
    assert check_win('O', board) == True

    # Test vertical win
    board = [['X', 'O', ' '],
             ['X', 'O', ' '],
             ['X', ' ', ' ']]
    assert check_win('X', board) == True

    board = [['O', 'X', ' '],
             ['O', 'X', ' '],
             [' ', 'O', ' ']]
    assert check_win('O', board) == False

    # Test diagonal win (left to right)
    board = [['X', 'O', ' '],
             ['O', 'X', ' '],
             [' ', ' ', 'X']]
    assert check_win('X', board) == True

    # Test diagonal win (right to left)
    board = [[' ', 'O', 'X'],
             [' ', 'X', 'O'],
             ['X', ' ', ' ']]
    assert check_win('X', board) == True

def test_edge_cases():
    # Test empty board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    assert check_win('X', board) == False
    assert check_draw(board) == False

    # Test full board without a win
    board = [['X', 'O', 'X'],
             ['O', 'X', 'O'],
             ['X', 'O', 'X']]
    assert check_win('X', board) == True
    assert check_draw(board) == False


def test_all_wins() -> ' ':
    # test_row_wins()
    # test_column_wins()
    # test_diagonal_wins()
    test_win_conditions()
    test_edge_cases()
    print("All tests PASS")