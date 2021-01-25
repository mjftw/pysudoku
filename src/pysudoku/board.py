from typing import List, NoReturn, Union
class Board:
    def __init__(self, size: int = 9, cell_size: int = 3):
        self._assert_valid_cell_size(size, cell_size)

        self.tiles = [[0 for _ in range(size)] for _ in range(size)]
        self.cell_size = cell_size

    def rows(self):
        return len(self.tiles)

    def cols(self):
        return len(self.tiles[0]) if self.tiles else 0

    def _assert_valid_cell_size(self, size: int, cell_size: int):
        if size % cell_size != 0:
            raise AttributeError('cell_size must be multiple of size')

    def _assert_in_bounds(self, col: int, row: int) -> Union[NoReturn, None]:
        if (
            col < 0 or
            row < 0 or
            row >= self.rows() or
            col >= self.cols()
        ):
            raise RuntimeError(f'Coordinates out of bounds: [{col}, {row}]')

    def _assert_value_in_range(self, value) -> Union[NoReturn, None]:
        if (value < 1 or
            value > self.rows() or
            value > self.cols()
        ):
            raise RuntimeError(f'Value out of bounds: {value}')


    def set_tile(self, col: int, row: int, value: int):
        self._assert_in_bounds(col, row)
        self._assert_value_in_range(value)

        self.tiles[row][col] = value

    def get_tile(self, col: int, row: int) -> int:
        self._assert_in_bounds(col, row)

        return self.tiles[row][col]

