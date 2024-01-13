from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for items in shift:
            if items[0] == 0:
                total_shift -= items[1]
            else:
                total_shift += items[1]

        if total_shift > 0:
            total_shift = total_shift % len(s)
            total_shift = len(s) - total_shift
            r_first = s[0:total_shift]
            r_second = s[total_shift:]
            return r_second + r_first

        elif total_shift < 0:
            total_shift = (-total_shift % len(s))
            l_first = s[0:total_shift]
            l_second = s[total_shift:]
            return l_second + l_first

        else:
            return s


# s = "abc"
# shift = [[0, 1], [1, 2]]

# s = "abcdefg"
# shift = [[1, 1], [1, 1], [0, 2], [1, 3]]

s = "wpdhhcj"
shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]

result = Solution()
print(result.stringShift(s, shift))
