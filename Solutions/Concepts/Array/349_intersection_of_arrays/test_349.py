from problem_349_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1,2,2,1], [2,2], [2]),
    ([4,9,5], [9,4,9,8,4], [9, 4])
])

def testIntersection(nums1, nums2, expected):
    assert Solution.intersection("", nums1, nums2) == expected