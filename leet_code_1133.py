import collections
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        sorted_x = sorted(counter.items(), key=lambda item:item[0])
        for item in reversed(sorted_x):
            if item[1] == 1:
                return item[0]
        return -1


result = Solution()

nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(result.largestUniqueNumber(nums))
