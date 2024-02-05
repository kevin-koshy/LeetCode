from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def max_sum(arr, k, dp, start):
            N = len(arr)
            if start >= N:
                return 0
            if dp[start] != -1:
                return dp[start]

            curr_max, ans = 0, 0
            end = min(N, start + k)
            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                ans = max(ans, curr_max * (i - start + 1) + max_sum(arr, k, dp, i + 1))
            dp[start] = ans
            return dp[start]

        dp = [-1] * len(arr)

        return max_sum(arr, k, dp, 0)


solution = Solution()
arr1 = [1, 15, 7, 9, 2, 5, 10]
k1 = 3
print(solution.maxSumAfterPartitioning(arr1, k1))
