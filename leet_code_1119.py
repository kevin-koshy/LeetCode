class Solution:
    def removeVowels(self, s: str) -> str:
        return s.translate({ord(i):None for i in 'aeiou'})




s = "leetcodeisacommunityforcoders"
result = Solution()
print(result.removeVowels(s))