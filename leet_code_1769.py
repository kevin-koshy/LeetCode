from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result_array = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] != '0':
                    count += abs(i-j)
            result_array.append(count)

        return result_array

boxes1 = "001011"

result = Solution()
print(result.minOperations(boxes1))
