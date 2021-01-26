from typing import List, NoReturn, Tuple, Union
from dataclasses import dataclass, field
import os
from math import sqrt


def empty_tiles(size: int) -> List[List[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]


@dataclass(frozen=True)
class Board:
    tiles: List[List[int]] = field(default_factory=lambda: empty_tiles(9))

    def __post_init__(self):
        _assert_valid_tiles(self.tiles)

    @property
    def size(self):
        return len(self.tiles)

    @property
    def cell_size(self):
        return int(sqrt(len(self.tiles)))


def _assert_valid_tiles(tiles):
    _assert_board_square(tiles)
    _assert_valid_size(tiles)
    _assert_valid_values(tiles)


def _assert_board_square(tiles) -> Union[NoReturn, None]:
    rows = len(tiles)

    if not rows:
        raise AttributeError('Empty board')

    if any(rows != len(col) for col in tiles):
        raise AttributeError('Board must be square')


def _assert_valid_size(tiles) -> Union[NoReturn, None]:
    if not float.is_integer(sqrt(len(tiles))):
        raise AttributeError('Board size must be a square number')


def _assert_valid_values(tiles: List[List[int]]) -> Union[NoReturn, None]:
    # Assumed square board at this point
    board_size = len(tiles)

    for row in tiles:
        for value in row:
            if value < 0 or value > board_size:
                raise AttributeError(f'Value out of bounds: {value}')


def _assert_valid_row(board: Board, row_idx: int):
    if not (0 <= row_idx < board.size):
        raise AttributeError(f'Row {row_idx} out of bounds')


def _assert_valid_col(board: Board, col_idx: int):
    if not ( 0 <= col_idx < board.size):
        raise AttributeError(f'Col {col_idx} out of bounds ')


def _assert_valid_coordinates(board: Board, col_idx: int, row_idx: int):
    _assert_valid_row(board, row_idx)
    _assert_valid_col(board, col_idx)


def set_tile(board: Board, col_idx: int, row_idx: int, value: int) -> Board:
    _assert_valid_coordinates(board, col_idx, row_idx)

    new_row = board.tiles[row_idx][:col_idx] + [value] + board.tiles[row_idx][col_idx+1:]
    new_tiles = (
        board.tiles[:row_idx] +
        [new_row] +
        board.tiles[row_idx+1:]
    )

    return Board(new_tiles)


def get_tile(board: Board, col_idx: int, row_idx: int) -> int:
    _assert_valid_coordinates(board, col_idx, row_idx)
    return board.tiles[row_idx][col_idx]


def value_in_row(board: Board, value: int, row_idx: int) -> bool:
    return value in board.tiles[row_idx]


def value_in_col(board: Board, value: int, col_idx: int) -> bool:
    return any(value == row[col_idx] for row in board.tiles)


def value_in_local_cell(board: Board, value: int, col_idx: int, row_idx: int) -> bool:
    cell_row_start = (row_idx // board.cell_size) * board.cell_size
    cell_col_start = (col_idx // board.cell_size) * board.cell_size
    cell_row_end = cell_row_start + board.cell_size
    cell_col_end = cell_col_start + board.cell_size

    cell_values = [val for row in board.tiles[cell_row_start:cell_row_end] for val in row[cell_col_start:cell_col_end]]
    return value in cell_values


def valid_placement(board: Board, value: int, col_idx: int, row_idx: int) -> bool:
    return not (
        value_in_row(board, value, row_idx) or
        value_in_col(board, value, col_idx) or
        value_in_local_cell(board, value, col_idx, row_idx)
    )


def print_board(board: Board):
    padsize = len(str(board.size))
    output_rows = []
    row_str = ''
    for row_idx, row in enumerate(board.tiles):
        if row_idx > 0:
            output_rows.append(row_str)
            row_str = ''
            if row_idx % board.cell_size == 0:
                row_str += '-' * len(output_rows[0])
                output_rows.append(row_str)
                row_str = ''

        for col_idx, value in enumerate(row):
            # Set empty char as .
            to_print = value if value != 0 else '.'

            row_str += str(to_print).rjust(padsize + 1)
            if col_idx % board.cell_size == board.cell_size - 1 and col_idx < board.size - 1:
                row_str += ' ' + '|'.rjust(padsize-1)

    output_rows.append(row_str)

    print(os.linesep.join(output_rows))


def next_empty(board: Board) -> Union[Tuple[int, int], None]:
    for row_idx in range(board.size):
        for col_idx in range(board.size):
            if get_tile(board, col_idx, row_idx) == 0:
                return (col_idx, row_idx)

    return None


def solve_backtrack(board: Board) -> Tuple[Board, bool]:
    empty_pos = next_empty(board)
    if not empty_pos:
        return board, True

    col_idx, row_idx = empty_pos
    possible_values = filter(lambda v: valid_placement(board, v, col_idx, row_idx), range(1, board.size+1))
    for value in possible_values:
        new_board = set_tile(board, col_idx, row_idx, value)
        new_board, solved = solve_backtrack(new_board)
        if solved:
            return new_board, True

    # Backtrack
    return board, False
