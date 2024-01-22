import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict1 = collections.Counter(nums)
        dup_num, missing_num = 0, 0
        num_list = [x+1 for x in range(0, len(nums))]
        for key, num in dict1.items():
            if num == 2:
                dup_num = key

        for item in num_list:
            if item not in dict1.keys():
                missing_num = item


        return [dup_num, missing_num]


# arr1 = [4, 8, 1, 5, 2, 7, 4, 6]
# arr1 = [1, 1]
arr1 = [2, 2]
result = Solution()
print(result.findErrorNums(arr1))
