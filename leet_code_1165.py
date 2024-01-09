class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        nums = list(range(0, 26))
        chars = list(keyboard)
        char_codes = dict(zip(chars, nums))
        moves = 0
        curr = 0
        value = 0
        for c in word:
            value = char_codes.get(c)
            moves += abs(curr - value)
            curr = value
        return moves


# keyboard = "abcdefghijklmnopqrstuvwxyz"
keyboard = "pqrstuvwxyzabcdefghijklmno"
# word = "cba"
word = "leetcode"

result = Solution()
print(result.calculateTime(keyboard, word))
