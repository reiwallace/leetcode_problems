from problem_165_retry_1 import Solution
import pytest

@pytest.mark.parametrize("version1, version2, expected", [
    ("1.2", "1.10", -1),
    ("1.01", "1.001", 0),
    ("1.0", "1.0.0.0", 0),
    ("7.5.2.4", "7.5.3", -1),
    ("1.0.1", "1", 1),
    ("1", "0", 1),
    ("0.1", "1.1", -1)
])

def testCompareVersion(version1, version2, expected):
    assert Solution.compareVersion("", version1, version2) == expected