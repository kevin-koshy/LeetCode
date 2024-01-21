from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result_arr = []
        j = 0
        min_ans = 0

        for i in range(len(arr)):
            j = i + 1
            while j < len(arr) + 1:
                result_arr.append(arr[i:j])
                j += 1
                min_ans += min(result_arr[-1])
        return min_ans % MOD


arr1 = [3, 1, 2, 4]
result = Solution()
print(result.sumSubarrayMins(arr1))
