import collections
from math import ceil


class Solution:
    def reorganizeString(self, s: str) -> str:
        d1 = collections.Counter(s)
        if max(d1.values()) > ceil(len(s) / 2):
            return ""
        max_count, max_char = 0, ''

        for char, count in d1.items():
            if count > max_count:
                max_count = count
                max_char = char

        t1 = [''] * len(s)
        i = 0
        ans = []

        while d1[max_char] != 0:
            t1[i] = max_char
            i += 2
            d1[max_char] -= 1

        for char, count in d1.items():
            while count > 0:
                if i >= len(s):
                    i = 1
                t1[i] = char
                i += 2
                count -= 1

        return ''.join(t1)


s1 = "aabbcc"

result = Solution()
print(result.reorganizeString(s1))
