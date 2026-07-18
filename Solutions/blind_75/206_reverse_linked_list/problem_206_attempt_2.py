from typing import Optional
from listNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        while head:
            new = head
            head = head.next
            new.next = ans
            ans = new
        return ans