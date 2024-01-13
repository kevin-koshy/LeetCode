from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1,len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True


intervals = [[7,10],[2,4]]

result = Solution()
print(result.canAttendMeetings(intervals))
