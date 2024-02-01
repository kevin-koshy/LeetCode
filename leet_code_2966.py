from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [nums[i:i + 3] for i in range(0, len(nums), 3)]
        for item in ans:
            if item[1] - item[0] > k or item[2] - item[1] > k or item[2] - item[0] > k:
                return []
        return ans


result = Solution()
# nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
nums1 =  [1,3,3,2,7,3]
# k1 = 2
k1 = 3

print(result.divideArray(nums1, k1))
