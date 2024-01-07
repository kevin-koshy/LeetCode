from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pass

nums1 = [-2,1,-3,4,-1,2,1,-5,4]

result = Solution()
print(result.maxSubArray(nums1))