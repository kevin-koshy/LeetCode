from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while (i <= j):
            s[i], s[j] = self.swap(s[i], s[j])
            i += 1
            j -= 1
        print(s)

    def swap(self, x, y):
        return (y, x)

result = Solution()
s = ["h","e","l","l","o"]
result.reverseString(s)