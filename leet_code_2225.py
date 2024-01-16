from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = {}
        for items in matches:
            if items[0] in ans:
                ans[items[0]] += 0
            else:
                ans[items[0]] = 0

            if items[1] in ans:
                ans[items[1]] += 1
            else:
                ans[items[1]] = 1

        w_list = []
        l_list = []
        for key in ans:
            if ans[key] == 0:
                w_list.append(key)
            if ans[key] == 1:
                l_list.append(key)

        return[sorted(w_list), sorted(l_list)]




result = Solution()
matches1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(result.findWinners(matches1))
