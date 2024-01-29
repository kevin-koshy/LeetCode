from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cum_sum = 0, 0
        sum_dict = {0: 1}
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in sum_dict.keys():
                count += sum_dict[cum_sum - k]
            if cum_sum in sum_dict.keys():
                sum_dict[cum_sum] += 1
            else:
                sum_dict[cum_sum] = 1
        return count

        # count = 0
        # cum_sum = [0] * (len(nums)+1)
        # cum_sum[0] = 0
        # for i in range(1, len(nums)+1):
        #     cum_sum[i] = cum_sum[i - 1] + nums[i - 1]
        #
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)+1):
        #         if cum_sum[j] - cum_sum[i] == k:
        #             count += 1
        # return count


#         answer = 0
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[j]
#                 if total == k:
#                     answer += 1
#         return answer

nums1 = [1, 1, 1]
k1 = 2
result = Solution()
print(result.subarraySum(nums1, k1))
