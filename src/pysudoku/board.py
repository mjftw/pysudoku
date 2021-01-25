from typing import List, NoReturn, Union
from dataclasses import dataclass, field
from numpy import matrix

def empty_tiles(size: int) -> List[List[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]

@dataclass(frozen=True)
class Board:
    tiles: List[List[int]] = field(default_factory=lambda: empty_tiles(9))
    cell_size: int = 3

    def __post_init__(self):
        _assert_valid_params(self.tiles, self.cell_size)

    @property
    def size(self):
        return len(self.tiles)


def _assert_valid_params(tiles, cell_size):
        _assert_board_square(tiles)
        _assert_valid_cell_size(tiles, cell_size)
        _assert_valid_values(tiles)

def _assert_board_square(tiles) -> Union[NoReturn, None]:
    rows = len(tiles)

    if not rows:
        raise AttributeError('Empty board')

    if any(rows != len(col) for col in tiles):
        raise AttributeError('Board must be square')


def _assert_valid_cell_size(tiles, cell_size) -> Union[NoReturn, None]:
    if len(tiles) % cell_size != 0:
        raise AttributeError('cell_size must be multiple of size')


def _assert_valid_values(tiles: List[List[int]]) -> Union[NoReturn, None]:
    # Assumed square board at this point
    board_size = len(tiles)

    for row in tiles:
        for value in row:
            if value < 0 or value > board_size:
                raise AttributeError(f'Value out of bounds: {value}')

def _assert_valid_coordinates(board: Board, row: int, col: int):
    if not (0 <= row < board.size) or (not 0 <= col < board.size):
        raise AttributeError('Coordinates out of range')

def set_tile(board: Board, col: int, row: int, value: int) -> Board:
    _assert_valid_coordinates(board, row, col)

    new_row = board.tiles[row][:col] + [value] + board.tiles[row][col+1:]
    new_tiles = (
        board.tiles[:row] +
        [new_row] +
        board.tiles[row+1:]
    )

    return Board(
        tiles=new_tiles,
        cell_size=board.cell_size
    )

def get_tile(board: Board, col: int, row: int) -> int:
    _assert_valid_coordinates(board, row, col)
    return board.tiles[row][col]

def str_board(board: Board) -> str:
    return str(matrix(board.tiles))