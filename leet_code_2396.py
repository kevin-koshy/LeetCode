class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def get_base_rep(num, base):
            res = ""
            while num:
                num, rem = divmod(num, base)
                res = res + str(rem)
            print(res)
            return res[::-1] == res

        # get_base_rep(9,2)

        for i in range(2, n - 2 + 1):
            if not get_base_rep(n, i):
                return False

        return True


result = Solution()
print(result.isStrictlyPalindromic(9))
