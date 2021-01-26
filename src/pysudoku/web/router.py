from typing import List
from fastapi import HTTPException
from pysudoku.web.app import app
from pysudoku.core.board import Board, solve_backtrack
from pysudoku.web.models import BoardModel


@app.post("/solve")
def solve(board: BoardModel):
    try:
        b = Board(board.board)
    except AttributeError as e:
        # Alert API user of any validation errors found creating the board
        raise HTTPException(status_code=422, detail=str(e))

    solution, solved = solve_backtrack(b)
    return {'solution': solution.tiles, 'solved': solved}