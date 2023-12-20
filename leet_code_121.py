from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return  max_profit



result = Solution()
prices = [7,6,4,3,1]

print(result.maxProfit(prices))