class Solution:
    def countLetters(self, s: str) -> int:
        count = 1
        index = 0
        word = {}
        word_key = 1
        while index < len(s) - 1:
            if s[index] == s[index + 1]:
                count += 1
            else:
                count = 0
                word_key += 1
                count += 1
            word[word_key] = count
            index += 1
        ans = 0
        for key in word:
            ans += word[key] * (word[key] + 1)//2
        return ans

result = Solution()
s1 = "aaaba"
print(result.countLetters(s1))
