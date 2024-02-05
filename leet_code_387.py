import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_chars = collections.Counter(s)
        for i in range(len(s)):
            if dict_chars[s[i]] == 1:
                return i
        return -1



solution = Solution()
s1 = "loveleetcode"
print(solution.firstUniqChar(s1))