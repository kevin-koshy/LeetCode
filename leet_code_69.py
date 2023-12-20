class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0 or x == 1:
        #     return x
        # i = 2
        # while (i <= x // 2):
        #     if i * i > x:
        #         return i-1
        #     i += 1
        # return i-1

        if x < 2:
            return x

        left, right = 2, x // 2
        while (left <= right):
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid -1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right




result = Solution()

print(result.mySqrt(45))
