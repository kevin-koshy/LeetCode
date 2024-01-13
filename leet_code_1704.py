import collections


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        x = len(s)//2
        a = s[:x]
        b = s[x:]
        a_count = 0
        b_count = 0
        # a_dict = collections.Counter(a)
        # b_dict = collections.Counter(b)
        # for vowel in ['a','e', 'i', 'o', 'u']:
        #     if a_dict[vowel] != b_dict[vowel]:
        #         return False
        # return True
        for cha in a:
            if cha in ['a','e', 'i', 'o', 'u']:
                a_count += 1
        for chb in b:
            if chb in ['a','e', 'i', 'o', 'u']:
                b_count += 1
        return a_count == b_count



s = "book"

result = Solution()
print(result.halvesAreAlike(s))
