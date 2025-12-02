from problem_1342_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("num, expected", [
    (14, 6),
    (8, 4),
    (123, 12)
])

def test_number_of_steps(num, expected):
    assert Solution.numberOfSteps("", num) == expected