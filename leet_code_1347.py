import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        # count = 0
        # for key in t_dict:
        #     if key not in s_dict:
        #         count += t_dict[key]
        #     elif t_dict[key] > s_dict[key]:
        #         count += t_dict[key] - s_dict[key]
        diff = s_dict - t_dict
        return sum(diff.values())


# s = "bab"
# t = "aba"
s = "leetcode"
t = "practice"
# s = "anagram"
# t = "mangaar"
# s = "gctcxyuluxjuxnsvmomavutrrfb"
# t = "qijrjrhqqjxjtprybrzpyfyqtzf"

result = Solution()
print(result.minSteps(s, t))
