import math
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted([list(a) for a in zip(position, speed)], key=lambda x: x[0])
        POS = 0
        SPEED = 1

        fleets = 1
        print(sortedCars)

        for i in range(len(sortedCars) - 1, 0, -1):
            curCar = sortedCars[i]
            prevCar = sortedCars[i - 1]
            if curCar[SPEED] >= prevCar[SPEED]:
                fleets += 1
            elif curCar[POS] == prevCar[POS]: # Might cause problems
                continue
            else:
                speedDif = prevCar[SPEED] - curCar[SPEED] 
                distanceDif = curCar[POS] - prevCar[POS]
                distanceToEnd = target - curCar[POS]
                turnsToCatchUp = math.ceil(distanceDif / speedDif)
                turnsToEnd = math.ceil(distanceToEnd / curCar[SPEED])
                if turnsToCatchUp > turnsToEnd:
                    fleets += 1
                else:
                    prevCar[SPEED] = curCar[SPEED]
                    prevCar[POS] = curCar[POS] + turnsToCatchUp * curCar[SPEED]

        return fleets