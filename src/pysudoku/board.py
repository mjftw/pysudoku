from typing import NoReturn, Union


class Board:
    def __init__(self, size: int = 9):
        self.tiles = [[0 for _ in range(size)] for _ in range(size)]

    def rows(self):
        return len(self.tiles)

    def cols(self):
        return len(self.tiles[0]) if self.tiles else 0

    def _assert_in_bounds(self, col: int, row: int) -> Union[NoReturn, None]:
        if (
            col < 0 or
            row < 0 or
            row >= self.rows() or
            col >= self.cols()
        ):
            raise RuntimeError(f'Coordinates out of bounds: [{col}, {row}]')

    def set_tile(self, col: int, row: int, value: int):
        self._assert_in_bounds(col, row)
        if (value < 1 or
            value > self.rows() or
            value > self.cols()
        ):
            raise RuntimeError(f'Value out of bounds: {value}')

        self.tiles[row][col] = value

    def get_tile(self, col: int, row: int) -> int:
        self._assert_in_bounds(col, row)

        return self.tiles[row][col]