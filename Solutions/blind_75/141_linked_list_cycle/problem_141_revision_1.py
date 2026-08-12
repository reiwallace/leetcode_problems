from typing import Optional
from Solutions.blind_75.utils.listNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head and head.next != 1:
            temp = head.next
            head.next = 1
            head = temp
        return head != None and head.next == 1