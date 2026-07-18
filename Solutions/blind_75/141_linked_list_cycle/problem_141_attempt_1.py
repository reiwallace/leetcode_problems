from utils.listNode import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head != None and head.val != None:
            head.val = None
            head = head.next
        return bool(head)
        
        
