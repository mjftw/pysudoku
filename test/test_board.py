from pytest import raises
from pysudoku.board import Board


def test_board_should_start_empty():
    board = Board(9)
    assert board.tiles == [[0]*9]*9


def test_board_set_tile_sets_only_tile():
    board = Board(3)
    board.set_tile(1, 2, 3)
    assert board.tiles == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 3, 0],
    ]


def test_board_set_should_error_on_negative_col():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(-1, 1, 1)


def test_board_set_should_error_on_negative_row():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(1, -1, 1)


def test_board_set_should_error_on_row_too_high():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(1, 3, 1)


def test_board_set_should_error_on_col_too_high():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(3, 1, 1)



def test_board_set_should_error_on_negative_value():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(0, 0, -1)


def test_board_set_should_error_on_zero_value():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(0, 0, 0)


def test_board_set_should_error_on_value_too_high():
    board = Board(3)

    with raises(RuntimeError):
        board.set_tile(0, 0, 4)


def test_board_set_should_not_error_on_max_value():
    board = Board(3)
    board.set_tile(0, 0, 3)


def test_board_rows():
    board = Board(3)

    assert board.rows() == 3


def test_board_cols():
    board = Board(3)

    assert board.cols() == 3


def test_board_get():
    board = Board(3)
    board.set_tile(1, 2, 3)
    assert board.get_tile(1, 2) == 3


def test_board_get_should_error_on_negative_col():
    board = Board(3)

    with raises(RuntimeError):
        board.get_tile(-1, 1)


def test_board_get_should_error_on_negative_row():
    board = Board(3)

    with raises(RuntimeError):
        board.get_tile(1, -1)


def test_board_get_should_error_on_row_too_high():
    board = Board(3)

    with raises(RuntimeError):
        board.get_tile(1, 3)


def test_board_get_should_error_on_col_too_high():
    board = Board(3)

    with raises(RuntimeError):
        board.get_tile(3, 1)


def test_board_cols_safe_when_zero_size_board():
    board = Board(0)

    assert board.cols() == 0


def test_board_defaults_size_9():
    board = Board()
    assert board.rows() == 9 and board.cols() == 9


def test_board_no_error_when_size_multiple_of_cellsize():
    Board(99, 9)


def test_board_error_on_size_not_multiple_of_cellsize():
    with raises(AttributeError):
        Board(11, 2)

