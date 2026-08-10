from problem_1510_attempt_1 import Solution
import pytest   

@pytest.mark.parametrize("n, expected", [
    (1, True),
    (2, False),
    (4, True)
])

def testWinnerSquareGame(n, expected):
    assert Solution.winnerSquareGame("", n) == expected