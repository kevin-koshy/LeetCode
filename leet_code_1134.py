class Solution:
    def isArmstrong(self, n: int) -> bool:
        total = 0
        t = n
        count = len(str(n))
        while t > 0:
            t, y = divmod(t, 10)
            total += y ** count
        return total == n


n = 153
result = Solution()
print(result.isArmstrong(n))