from utils.listNode import ListNode
from typing import Optional

class Solution(object):
    def hasCycle(self, head):
        table = {}
        while head != None and not head in table:
            table[head] = 1
            head = head.next
        return bool(head)