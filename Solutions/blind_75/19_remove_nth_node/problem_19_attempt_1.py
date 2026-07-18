from utils.listNode import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1: return None
        length = 0
        nextNode = head
        while nextNode:
            length += 1
            nextNode = nextNode.next

        previous = head
        for i in range(length - n - 1):
            previous = previous.next    

        if previous == head:
            if n == 1: 
                head.next = None
            elif head.next.next == None or n == length:
                return head.next
        
        if previous.next != None:
            previous.next = previous.next.next

        return head