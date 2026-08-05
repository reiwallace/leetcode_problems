from problem_2073_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("tickets, k, expected", [
    ([2,3,2], 2, 6),
    ([5,1,1,1], 0, 8)
])

def testTimeRequiredToBuy(tickets, k, expected):
    assert Solution.timeRequiredToBuy("", tickets, k) == expected