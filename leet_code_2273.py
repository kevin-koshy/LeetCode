import collections
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        k = 0
        while i < len(words):
            if collections.Counter(words[i]) == collections.Counter(words[i-1]):
                words.remove(words[i])
                i -= 1
            i += 1
        return words

result = Solution()
words = ["abba","baba","bbaa","cd","cd"]
print(result.removeAnagrams(words))