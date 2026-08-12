from typing import Optional
from Solutions.blind_75.utils.listNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        while head and id(head) not in nodeSet:
            nodeSet.add(id(head))
            head = head.next
        return bool(head)