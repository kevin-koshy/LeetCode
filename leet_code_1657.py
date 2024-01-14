import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)


        list1 = []
        list2 = []

        for key in dict1:
            list1.append(dict1[key])
        for key in dict2:
            list2.append(dict2[key])

        return sorted(list1) == sorted(list2)


# word1 = "cabbba"
# word2 = "abbccc"
word1 = "uau"
word2 = "ssx"

result = Solution()

print(result.closeStrings(word1, word2))
