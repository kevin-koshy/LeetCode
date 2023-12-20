class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s1):
            ans = []
            for c in s1:
                if c != "#":
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ans

        s = helper(s)
        t = helper(t)
        return s == t


result = Solution()
s = "y#fo##f"
t = "y#f#o##f"

# s = "ab#c"
# t = "ad#c"
print(result.backspaceCompare(s, t))





