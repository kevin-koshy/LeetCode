from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '/', '*']:
                stack.append(tokens[i])
            else:
                elem1 = int(stack.pop())
                elem2 = int(stack.pop())
                if tokens[i] == '+':
                    ans = elem2 + elem1
                elif tokens[i] == '-':
                    ans = elem2 - elem1
                elif tokens[i] == "*":
                    ans = elem2 * elem1
                else:
                    ans = elem2 / elem1
                stack.append(ans)

        # return int(ans)
        return ans


result = Solution()
# tokens1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens1 = ["2", "1", "+", "3", "*"]
tokens1 = ["0","3","/"]
print(result.evalRPN(tokens1))
