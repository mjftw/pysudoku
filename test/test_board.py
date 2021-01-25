from pytest import raises
from pysudoku.board import Board, empty_tiles, get_tile, set_tile, str_board


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
    board = Board(empty_tiles(3))
    board = set_tile(board, 1, 2, 3)
    assert board.tiles == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 3, 0],
    ]


def test_set_tile_should_error_on_negative_col():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, -1, 1, 1)


def test_set_tile_should_error_on_negative_row():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, 1, -1, 1)


def test_set_tile_should_error_on_row_too_high():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, 1, 3, 1)


def test_set_tile_should_error_on_col_too_high():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, 3, 1, 1)



def test_set_tile_should_error_on_negative_value():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, 0, 0, -1)



def test_set_tile_should_error_on_value_too_high():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        set_tile(board, 0, 0, 4)


def test_set_tile_should_not_error_on_max_value():
    board = Board(empty_tiles(3))
    set_tile(board, 0, 0, 3)


def test_board_size():
    board = Board(empty_tiles(3))

    assert board.size == 3


def test_get_tile():
    board = Board(empty_tiles(3))
    board = set_tile(board, 1, 2, 3)
    assert get_tile(board, 1, 2) == 3


def test_get_tile_should_error_on_negative_col():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        get_tile(board, -1, 1)


def test_get_tile_should_error_on_negative_row():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        get_tile(board, 1, -1)


def test_get_tile_should_error_on_row_too_high():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        get_tile(board, 1, 3)


def test_get_tile_should_error_on_col_too_high():
    board = Board(empty_tiles(3))

    with raises(AttributeError):
        get_tile(board, 3, 1)


def test_board_no_error_when_size_multiple_of_cellsize():
    Board(empty_tiles(99), 9)


def test_board_error_on_size_not_multiple_of_cellsize():
    with raises(AttributeError):
        Board(empty_tiles(11), 2)

