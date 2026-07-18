from utils.listNode import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        idTable = {}
        while head != None and (not id(head) in idTable):
            idTable[id(head)] = 1
            head = head.next
        return bool(head)