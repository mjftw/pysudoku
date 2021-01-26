from typing import List
from pydantic import BaseModel


class BoardModel(BaseModel):
    board: List[List[int]]

    class Config:
        schema_extra = {
            'example': {
                'board': [
                    [0,0,0,0,0,0,0,0,7],
                    [0,0,0,0,0,0,0,3,4],
                    [0,0,7,0,0,3,0,0,0],
                    [0,8,0,4,0,0,0,0,9],
                    [2,4,1,7,5,0,0,0,3],
                    [0,5,8,0,0,4,0,0,0],
                    [0,1,9,8,0,0,7,0,2],
                    [7,0,3,0,1,0,0,5,0]
                ]
            }
        }

