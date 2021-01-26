from pysudoku.core.board import empty_tiles
from fastapi.testclient import TestClient


def test_post_to_solve_empty_board_should_have_solved_in_response(client: TestClient):
    response = client.post('/solve', json={'board': empty_tiles(9)})
    data = response.json()

    assert 'solved' in data
    assert data['solved'] == True


def test_post_to_solve_empty_board_should_solve_board(client: TestClient, solution_pair):
    response = client.post('/solve', json={'board': solution_pair.unsolved.tiles})
    data = response.json()

    assert 'solution' in data
    assert data['solution'] == solution_pair.solved.tiles