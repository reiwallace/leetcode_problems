class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Solution 2 (Transpose Matrix) (Without using extra space) (Time - 0(n^2) Space - O(1))
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]