from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpe = zip(position, speed)
        sorts = sorted(posSpe, key=lambda x: x[0], reverse=True)
        turns = []
        
        turns.append((target - sorts[0][0]) / sorts[0][1])
        fleets = 1
        for i in range(1, len(sorts)):
            turns.append((target - sorts[i][0]) / sorts[i][1])
            if turns[i - 1] >= turns[i]:
                turns[i] = turns[i - 1]
            else:
                fleets += 1

        return fleets
