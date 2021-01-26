from typing import List
from pydantic import BaseModel


class BoardModel(BaseModel):
    board: List[List[int]]