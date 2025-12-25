from problem_412_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (3, ["1","2","Fizz"]),
    (5, ["1","2","Fizz","4","Buzz"]),
    (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
])

def test_fizz_buzz(n, expected):
    assert Solution.fizzBuzz("", n) == expected