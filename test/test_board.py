from pytest import raises
import pytest
from pysudoku.core.board import (
    Board,
    empty_tiles,
    get_tile,
    set_tile,
    solve_backtrack,
    value_in_col,
    value_in_local_cell,
    value_in_row
)


def test_empty_tiles_should_fill_all_zero():
    assert empty_tiles(3) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_board_should_start_empty():
    board = Board(empty_tiles(9))
    assert board.tiles == [[0]*9]*9

def test_board_defaults_size_9():
    assert Board().size == 9

def test_board_defaults_cell_size_3():
    assert Board().cell_size == 3

def test_board_set_tile_sets_only_tile():
    board = Board(empty_tiles(4))
    board = set_tile(board, 1, 2, 3)
    assert board.tiles == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 0, 0],
    ]


def test_set_tile_should_error_on_negative_col():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, -1, 1, 1)


def test_set_tile_should_error_on_negative_row():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, 1, -1, 1)


def test_set_tile_should_error_on_row_too_high():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, 1, 4, 1)


def test_set_tile_should_error_on_col_too_high():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, 4, 1, 1)


def test_set_tile_should_error_on_negative_value():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, 0, 0, -1)



def test_set_tile_should_error_on_value_too_high():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        set_tile(board, 0, 0, 5)


def test_set_tile_should_not_error_on_max_value():
    board = Board(empty_tiles(4))
    set_tile(board, 0, 0, 4)


def test_board_size():
    board = Board(empty_tiles(4))

    assert board.size == 4


def test_get_tile():
    board = Board(empty_tiles(4))
    board = set_tile(board, 1, 2, 3)
    assert get_tile(board, 1, 2) == 3


def test_get_tile_should_error_on_negative_col():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        get_tile(board, -1, 1)


def test_get_tile_should_error_on_negative_row():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        get_tile(board, 1, -1)


def test_get_tile_should_error_on_row_too_high():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        get_tile(board, 1, 4)


def test_get_tile_should_error_on_col_too_high():
    board = Board(empty_tiles(4))

    with raises(AttributeError):
        get_tile(board, 4, 1)


def test_board_no_error_when_size_is_square_number():
    Board(empty_tiles(81))


def test_board_error_on_size_not_square_number():
    with raises(AttributeError):
        Board(empty_tiles(12))


def test_value_in_row_false():
    assert value_in_row(Board(), 5, 0) == False


def test_value_in_row_true():
    board = Board()
    board = set_tile(board, 1, 0, 3)
    assert value_in_row(board, 3, 0) == True


def test_value_in_col_false():
    assert value_in_col(Board(), 5, 0) == False


def test_value_in_col_true():
    board = Board()
    board = set_tile(board, 0, 1, 3)
    assert value_in_col(board, 3, 0) == True


def test_value_in_local_cell_false():
    assert value_in_local_cell(Board(), 5, 0, 0) == False


def test_value_in_local_cell_true():
    board = Board()
    board = set_tile(board, 8, 5, 3)
    assert value_in_local_cell(board, 3, 8, 5) == True

@pytest.mark.skip
def test_solve_backtrack(solution_pair):
    board, solved = solve_backtrack(solution_pair.unsolved)

    assert solved
    assert board == solution_pair.solved