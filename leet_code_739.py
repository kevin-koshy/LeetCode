from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [0]
        # ans = []
        # for i in range(1, len(temperatures)):
        #     if temperatures[i] > temperatures[i - 1]:
        #         ans.append(1)
        #     elif temperatures[i] <= temperatures[i - 1]:
        #         end = False
        #         count = 1
        #         ptr = temperatures[i]
        #         while ptr <= temperatures[i - 1] and not end:
        #             count += 1
        #             if i + count - 1 < len(temperatures):
        #                 ptr = temperatures[i + count - 1]
        #             else:
        #                 end = True
        #                 count = 0
        #         ans.append(count)
        #
        #     if i == len(temperatures) - 1:
        #         ans.append(0)
        # return ans

        ans = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, ind = stack.pop()
                ans[ind] = i - ind
            stack.append((temp, i))
        return ans


result = Solution()
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures1 = [30, 40, 50, 60]
# temperatures1 = [30, 60, 90]
# temperatures1 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
# temperatures1 = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
print(result.dailyTemperatures(temperatures1))
