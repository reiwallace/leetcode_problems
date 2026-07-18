from problem_21_attempt_1 import Solution
from listNode import ListNode
import pytest

@pytest.mark.parametrize("list1, list2, expected", [
    (ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None))), ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))),
    (None, ListNode(0, None), ListNode(0, None))
])

def testMergeTwoLists(list1, list2, expected):
    assert Solution.mergeTwoLists("", list1, list2) == expected