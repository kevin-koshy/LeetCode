from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[1])
        row_count = [0] * m
        col_count = [0] * n


        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if row_count[i] == 1 and col_count[j] == 1:
                        ans += 1

        return ans



result = Solution()
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(result.numSpecial(mat))