import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1 = collections.Counter(word1)
        d2 = collections.Counter(word2)
        diff1 = d1 - d2
        diff2 = d2 - d1

        for k1 in diff1.keys():
            for k2 in diff2.keys():
                if diff1[k1] > 3 or diff2[k2] > 3:
                    return False
        return True



result = Solution()
word1 = "aaaa"
word2 = "bccb"

print(result.checkAlmostEquivalent(word1, word2))