import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_falling_sum = sys.maxsize
        memo = [([None] * len(matrix)) for i in range(len(matrix))]
        for start_col in range(len(matrix)):
            min_falling_sum = min(min_falling_sum, self.find_min_falling_path_sum(matrix, 0, start_col, memo))
        return min_falling_sum

    def find_min_falling_path_sum(self, matrix, row: int, col: int, memo):
        if col < 0 or col == len(matrix):
            return sys.maxsize

        if row == len(matrix) - 1:
            return matrix[row][col]

        if memo[row][col] is not None:
            return memo[row][col]

        left = self.find_min_falling_path_sum(matrix, row + 1, col - 1, memo)
        middle = self.find_min_falling_path_sum(matrix, row + 1, col, memo)
        right = self.find_min_falling_path_sum(matrix, row + 1, col + 1, memo)

        min_sum = min(left, min(middle, right)) + matrix[row][col]
        memo[row][col] = min_sum
        return min_sum


result = Solution()
matrix1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(result.minFallingPathSum(matrix1))
