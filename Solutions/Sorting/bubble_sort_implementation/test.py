from bubble_char import sort
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 2, 10, 1], [1, 1, 2, 3, 10]),
    ([4, 9, 5, 9, 4, 9, 8, 4, 9, 4], [4, 4, 4, 4, 5, 8, 9, 9, 9, 9]),
    ([3, 2, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
    (["d", "c", "a", "h", "b"], ["a", "b", "c", "d", "h"])
])

def testSort(nums, expected):
    assert sort(nums) == expected