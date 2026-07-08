from typing import Optional
from listNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        ans = ListNode()
        ansNext = ans
        while stack:
            ansNext.next = ListNode(stack.pop(), None)
            ansNext = ansNext.next

        return ans.next