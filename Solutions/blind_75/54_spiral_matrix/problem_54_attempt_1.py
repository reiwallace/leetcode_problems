from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new = []
        x = 0
        y = 0
        maxX = len(matrix) - 1
        maxY = len(matrix[0]) - 1
        total = (maxX + 1) * (maxY + 1)
        direction = "right"

        for i in range(total):
            new.append(matrix[x][y])
            matrix[x][y] = None

            for i in range(4):
                match direction:
                    case "right":
                        y += 1
                        if y > maxY or matrix[x][y] == None:
                            direction = "down"
                            y -= 1

                    case "left":
                        y -= 1
                        if y < 0 or matrix[x][y] == None:
                            direction = "up"
                            y += 1

                    case "down":
                        x += 1
                        if x > maxX or matrix[x][y] == None:
                            direction = "left"
                            x -= 1

                    case "up":
                        x -= 1
                        if x < 0 or matrix[x][y] == None:
                            direction = "right"
                            x += 1

                if matrix[x][y] != None:
                    break

        return new