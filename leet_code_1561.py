from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        ans = []
        def get_chunks(l):
            a = l.pop(-1)
            b = l.pop(-1)
            c = l.pop(0)
            return [a, b, c]

        while piles:
            ans.append(get_chunks(piles))

        return sum([x[1] for x in ans])

# class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
#         piles = sorted(piles)
#         ans = 0
#
#         for i in range(len(piles)//3, len(piles), 2):
#             ans += piles[i]
#         return ans




piles1 = [2,4,1,2,7,8]
piles2 = [2,4,5]
piles3 = [9,8,7,6,5,1,2,3,4]
result = Solution()
print(result.maxCoins(piles3))