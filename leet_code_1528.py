from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['']*len(s)
        for i, letter in enumerate(s):
            ans[indices[i]] = letter

        ans = "".join(ans)
        return ans


result = Solution()

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(result.restoreString(s, indices))