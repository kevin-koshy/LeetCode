from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        for i, elem in enumerate(nums2):
            ans[elem] = i
        return [ans[x] for x in nums1]


result = Solution()
nums1 = [40, 40]
nums2 = [40, 40]
x = result.anagramMappings(nums1, nums2)
print(x)