from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        def optimum_height(a, b):
            return min(max(a), max(b))

        def sum_lists(a):
            return sum(sum(x) for x in a)

        def get_building_height(grid, r_index, c_index):
            cols = []
            for item in grid:
                cols.append(item[c_index])
            return grid[r_index], cols

        # print(get_building_height(grid, 0,0))
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                vals = get_building_height(grid, row, col)
                ans += optimum_height(vals[0], vals[1])

        return ans - sum_lists(grid)


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
result = Solution()
print(result.maxIncreaseKeepingSkyline(grid))
