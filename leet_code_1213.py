import collections
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr = arr1 + arr2 + arr3
        dict_arr = collections.Counter(arr)
        ans = []
        for key in dict_arr:
            if dict_arr.get(key) >= 3:
                ans.append(key)
        return sorted(ans)


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = Solution()
print(result.arraysIntersection(arr1, arr2, arr3))
