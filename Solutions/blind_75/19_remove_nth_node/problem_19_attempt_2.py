from utils.listNode import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1: return None
        previousN = head
        count = 0
        node = head.next
        while node:
            count += 1
            if count == n and node.next != None:
                count = 0
                previousN = node
            node = node.next

        print(previousN)
        if previousN == head:
            if n == 1: 
                head.next = None
            elif head.next.next == None or n == 3:
                return head.next


        if previousN.next != None:
            previousN.next = previousN.next.next

        return head
        
