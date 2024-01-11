from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # result = [0] * length
        # for item in updates:
        #     i, j, k = item[0], item[1], item[2]
        #     for x in range(i, j + 1):
        #         result[x] += k
        # print(result)
        arr = [0] * length
        for item in updates:
            start, end, value = item[0], item[1], item[2]
            arr[start] += value
            if end + 1 < length:
                arr[end+1] -= value
        for i in range(1, len(arr)):
            arr[i] = arr[i-1]+arr[i]
        return arr


result = Solution()
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(result.getModifiedArray(length, updates))
