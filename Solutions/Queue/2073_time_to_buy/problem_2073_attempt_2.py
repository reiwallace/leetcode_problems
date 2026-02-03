from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        iterations = 0
        pointer = -1
        while 1 != 0:
            if tickets[k] <= 0:
                break

            if pointer < len(tickets) - 1:
                pointer += 1
            else:
                pointer = 0

            if tickets[pointer] <= 0:
                continue

            tickets[pointer] -= 1
            iterations += 1
            
        return iterations