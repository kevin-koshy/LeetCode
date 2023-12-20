from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        char_array = []
        lines, width = 1, 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return [lines, width]


result = Solution()
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
print(result.numberOfLines(widths, s))
