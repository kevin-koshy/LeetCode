from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_seq = 1

                while curr_num+1 in nums:
                    curr_num += 1
                    curr_seq += 1
                longest_seq = max(longest_seq, curr_seq)
        return longest_seq


result = Solution()
nums1 = [100, 4, 200, 1, 3, 2]
print(result.longestConsecutive(nums1))
