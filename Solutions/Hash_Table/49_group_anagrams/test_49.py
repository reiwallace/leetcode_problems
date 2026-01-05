from problem_49_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("strs, expected", [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]])
])

def testGroupAnagrams(strs, expected):
    assert Solution.groupAnagrams("", strs) == expected