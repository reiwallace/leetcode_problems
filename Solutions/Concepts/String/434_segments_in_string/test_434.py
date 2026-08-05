from problem_434_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("Hello, my name is John", 5),
    ("Hello", 1),
    ("", 0),
    (", , , ,        a, eaefa", 6)
])

def testCountSegments(s, expected):
    assert Solution.countSegments("", s) == expected