from typing import Optional
from listNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newListHead = ListNode()
        nextNode = newListHead
        while list1 and list2:
            if list1.val >= list2.val:
                nextNode.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                nextNode.next = list1
                list1 = list1.next
            nextNode = nextNode.next

        while list1:
            nextNode.next = list1
            list1 = list1.next
            nextNode = nextNode.next

        while list2:
            nextNode.next = list2
            list2 = list2.next
            nextNode = nextNode.next

        return newListHead.next
                