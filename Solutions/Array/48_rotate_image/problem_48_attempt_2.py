from typing import List

class Solution:
    # Time complexity O(n^2), Space Complexity O(n^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        "Index becomes row"
        "Reverse row becomes index"
        matrixLen = len(matrix)
        newMatrix = [[0 for x in range(matrixLen)] for y in range(matrixLen)]
        for row in range(matrixLen):
            for n in range(len(matrix[row])):
                newMatrix[n][-row - 1] = matrix[row][n]

        matrix[:] = newMatrix
        return matrix

        