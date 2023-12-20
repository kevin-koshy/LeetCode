class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        def rotate(s):
            x = s[1:] + s[:1]
            return x

        i = 0
        while i < len(s):
            s = rotate(s)
            if s == goal:
                return True
            i += 1
        return False



result = Solution()
s = "abcde"
goal = "abced"
print(result.rotateString(s, goal))