from typing import List

class Solution:
    # Time complexity O(n^2), Space Complexity O(n^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        "Index becomes row"
        "Reverse row becomes index"
        newMatrix = []
        for row in range(len(matrix)):
            newMatrix.append([])
            for n in matrix[row]:
                newMatrix[row].append(n)

        for row in range(len(matrix)):
            for n in range(len(matrix[row])):
                newMatrix[n][-row - 1] = matrix[row][n]

        matrix[:] = newMatrix
        return matrix

        