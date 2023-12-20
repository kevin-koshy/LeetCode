import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = collections.Counter(s)
        y = collections.Counter(t)
        return collections.Counter(s) == collections.Counter(t)


result = Solution()
s = "anagram"
t = "nagaram"

print(result.isAnagram(s,t))