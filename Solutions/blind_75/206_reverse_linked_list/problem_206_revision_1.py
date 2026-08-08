from typing import Optional
from Solutions.blind_75.utils.listNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            temp = head
            head = head.next
            temp.next = previous
            previous = temp
        return previous