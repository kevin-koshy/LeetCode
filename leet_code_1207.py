import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = collections.Counter(arr)
        list1 = []
        for key in dict1:
            list1.append(dict1.get(key))

        return len(set(list1)) == len(list1)

result = Solution()
arr1 = [1, 2, 2, 1, 1, 3]
print(result.uniqueOccurrences(arr1))
