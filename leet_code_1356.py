import collections
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def binary_rep(num):
            return "{0: b}".format(num)

        binary_collection = []
        for num in arr:
            r = binary_rep(num)
            # binary_collection[num] = r.count('1')
            binary_collection.append([num, r.count('1')])
        print(binary_collection)
        if all(v == 1 for v in binary_collection):
            return sorted(arr)

        sorted_result = sorted(binary_collection.items(), key=lambda item:item[1])
        print(sorted_result)
        sorted_result = [i[0] for i in sorted_result]
        return sorted_result


result = Solution()
# arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr = [10000,10000]
print(result.sortByBits(arr))