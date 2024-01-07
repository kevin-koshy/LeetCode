from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_arr = []
        col_arr = []
        for item in grid:
            row_arr.append(sum(item))

        t_grid = list(zip(*grid))
        for item in t_grid:
            col_arr.append(sum(item))

        # def create_array(arr, row=True):
        #     res_arr = []
        #     if row:
        #         dim = len(grid[0])
        #     else:
        #         dim = len(grid)
        #     for elem in arr:
        #         x = [elem] * dim
        #         res_arr.append(x)
        #     return res_arr
        #
        # row_ones = create_array(row_arr)
        # col_ones = [list(a) for a in list(zip(*create_array(col_arr, False)))]
        #
        # row_dim = len(grid[0])
        # col_dim = len(grid)
        #
        # row_zeros = [[row_dim-y for y in x] for x in row_ones]
        # col_zeros = [[col_dim-y for y in x] for x in col_ones]
        #
        # row_sum = [zip(*t) for t in zip(row_ones, col_ones)]
        # row_sum = [map(sum, list(x)) for x in row_sum]
        #
        # col_sum = [zip(*t) for t in zip(row_zeros, col_zeros)]
        # col_sum = [map(sum, list(x)) for x in col_sum]
        #
        # ones = []
        # zeros = []
        #
        # for item in row_sum:
        #     ones.append(list(item))
        #
        # for item in col_sum:
        #     zeros.append(list(item))
        # ans = []
        #
        # for item in list(zip(ones, zeros)):
        #     ans.append([a-b for a, b in zip(item[0], item[1])])

        row_dim = len(grid)
        col_dim = len(grid[0])
        diff = []

        for i in range(row_dim):
            x = []
            for j in range(col_dim):
                x.append(2 * row_arr[i] + 2 * col_arr[j] - row_dim - col_dim)
                # diff[i][j] = 2 * row_arr[i] + 2 * col_arr[j] - row_dim - col_dim
            diff.append(x)
        return diff


# grid_1 = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
grid_1 = [[1,1,1],[1,1,1]]
result = Solution()
print(result.onesMinusZeros(grid_1))
