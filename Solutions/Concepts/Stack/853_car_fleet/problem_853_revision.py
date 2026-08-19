import math
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted(list(zip(position, speed)), key=lambda x: x[0])
        POS = 0
        SPEED = 1

        fleets = 1
        print(sortedCars)

        for i in range(len(sortedCars) - 1):
            curCar = sortedCars[i]
            nextCar = sortedCars[i + 1]
            if curCar[SPEED] <= nextCar[SPEED]:
                fleets += 1
            elif curCar[POS] == nextCar[POS]:
                fleets += 1
            else:
                speedDif = curCar[SPEED] - nextCar[SPEED]
                distanceDif = nextCar[POS] - curCar[POS]
                distanceToEnd = target - nextCar[POS]
                turnsToCatchUp = math.ceil(distanceDif / speedDif)
                turnsToEnd = math.ceil(distanceToEnd / nextCar[SPEED])
                if turnsToCatchUp > turnsToEnd:
                    fleets += 1

        return fleets