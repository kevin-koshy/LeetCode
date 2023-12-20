class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s1):
            i = 0
            while i < len(s1):
                if s1[i] == "#" and i > 0:
                    s1 = s1[:i-1]+ s1[i+1:]
                    i -= 2
                i+=1
            print(s1)
            return s1

        s = helper(s)
        t = helper(t)
        return s == t


result = Solution()
s = "y#fo##f"
t = "y#f#o##f"
print(result.backspaceCompare(s, t))





