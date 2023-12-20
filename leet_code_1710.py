from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box_type = sorted(boxTypes, key=lambda x: -x[0])
        space = 0
        while space < truckSize:
            for item in sorted_box_type:
                truckSize = truckSize - item[0]



result = Solution()

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(result.maximumUnits(boxTypes, truckSize))