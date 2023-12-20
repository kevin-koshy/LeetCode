from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cum_list = [sum(nums[0:x:1]) for x in range(0,len(nums)+1)]
        return cum_list[1:]

result = Solution()
nums = [1,2,3,4]
print(result.runningSum(nums))