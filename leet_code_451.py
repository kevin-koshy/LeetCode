import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = collections.Counter(s)
        s_dict = dict(sorted(s_dict.items(), key=lambda x: x[1], reverse=True))

        ans = ''
        for key in s_dict:
            repeat = s_dict[key]
            i = 0
            while i < repeat:
                ans += key
                i += 1
        return ans


solution = Solution()
s1 = "Aabb"
print(solution.frequencySort(s1))
