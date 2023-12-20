class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def keep_dividing(dividend, divisor):
            while dividend % divisor == 0:
                dividend = dividend // divisor
            return dividend

        for nums in [2, 3, 5]:
            n = keep_dividing(n, nums)
        return n == 1

result = Solution()

print(result.isUgly(15))