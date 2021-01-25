from typing import List


class Board:
    def __init__(self, size):
        self.tiles = [[0 for _ in range(size)] for _ in range(size)]

    def rows(self):
        return len(self.tiles)

    def cols(self):
        return len(self.tiles[0]) if self.tiles else 0

    def set_tile(self, col: int, row: int, value: int):
        if (col < 0 or
            row < 0 or
            row >= len(self.tiles) or
            col >= len(self.tiles[0])
        ):
            raise RuntimeError(f'Coordinates out of bounds: [{col}, {row}]')

        self.tiles[row][col] = value
