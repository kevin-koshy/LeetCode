from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Initialize results with an empty string
        # from which to build all future results
        results = [""]
        best = 0
        for word in arr:
            # We only want to iterate through results
            # that existed prior to this loop
            for i in range(len(results)):
                # Form a new result combination and
                # use a set to check for duplicate characters
                new_res = results[i] + word
                if len(new_res) != len(set(new_res)):
                    continue

                # Add valid options to results and
                # keep track of the longest so far
                results.append(new_res)
                best = max(best, len(new_res))
        return best


result = Solution()

arr1 = ["cha", "r", "act", "ers"]
# arr1 = ["un","iq","ue"]
# arr1 = ["abcdefghijklmnopqrstuvwxyz"]
# arr1 = ["aa", "bb"]
# arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
print(result.maxLength(arr1))
