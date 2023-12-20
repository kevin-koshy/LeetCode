from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        for i in range(len(nums1)-1,-1,-1):

            if p2 < 0:
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -=1
            else:
                nums1[i] = nums2[p2]
                p2 -=1



        print(nums1)

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

result = Solution()
result.merge(nums1,m,nums2,n)