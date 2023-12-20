class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_map = {"{": "}", "[": "]", "(": ")̵"}
        stack = []
        open_brackets = ("{", "[", "(")

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False

        return stack == []


result = Solution()
print(result.isValid("{[]}"))
