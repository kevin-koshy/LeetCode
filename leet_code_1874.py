from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # x = sorted(range(len(nums2)), reverse=True, key=lambda x: nums2[x])
        # x = [(b, a) for a, b in zip(x, range(len(x)))]
        # x = sorted(x, key=lambda x:x[1])
        # x = list(zip(*x))[0]
        # y = []
        # nums1_sorted = sorted(nums1, reverse=False)
        # for i, _ in enumerate(nums1_sorted):
        #     y.append(nums1_sorted[x[i]])
        # ans = sum([(a*b) for a, b in zip(nums2, y)])
        # return ans
        nums1 = sorted(nums1, reverse=True)
        nums2 = sorted(nums2, reverse=False)
        ans = sum((x*y) for x, y in zip(nums1, nums2))
        return ans

result = Solution()
# nums1 = [5, 3, 4, 2]
# nums2 = [4, 2, 2, 5]
# nums1 = [2,1,4,5,7]
nums1 = [2,1,5,4,4]
# nums2 = [3,2,4,8,6]
nums2 = [3,2,9,2,10]


print(result.minProductSum(nums1, nums2))
