from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        iterations = 0
        while queue:
            current = queue.popleft() - 1
            if current > 0: 
                queue.append(current)

            if k == 0:
                if current <= 0:
                    iterations += 1
                    break
                else:
                    k = len(queue) - 1
            else:
                k -= 1
            iterations += 1

        return iterations
