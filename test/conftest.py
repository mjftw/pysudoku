
from dataclasses import dataclass
from pytest import fixture
from pysudoku.board import Board


@dataclass
class Solution:
    unsolved: Board
    solved: Board


@fixture
def solution_pair() -> Solution:
    unsolved = Board([
        [0,0,9,0,4,0,0,0,0],
        [0,8,0,0,9,7,0,0,2],
        [0,4,0,8,5,0,0,0,0],
        [0,0,0,7,0,0,9,6,0],
        [0,0,0,0,0,8,0,7,1],
        [0,0,0,0,6,0,0,0,0],
        [9,0,0,2,0,4,0,0,8],
        [0,1,0,0,0,0,4,2,7],
        [0,0,0,0,8,5,0,0,6],
    ])
    solved = Board([
        [7,3,9,6,4,2,8,1,5],
        [5,8,1,3,9,7,6,4,2],
        [6,4,2,8,5,1,7,3,9],
        [2,5,8,7,1,3,9,6,4],
        [3,9,6,4,2,8,5,7,1],
        [1,7,4,5,6,9,2,8,3],
        [9,6,3,2,7,4,1,5,8],
        [8,1,5,9,3,6,4,2,7],
        [4,2,7,1,8,5,3,9,6],
    ])

    return Solution(unsolved, solved)