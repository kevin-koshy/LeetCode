from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        result = []
        seen_array = []
        index_array = []

        def get_index(target_list, elem):
            result_array = []
            for i, j in enumerate(target_list):
                if j == elem:
                    result_array.append(i)
            return result_array

        def split_list(target_list, n):
            chunks = [target_list[x:x + n] for x in range(0, len(target_list), n)]
            return chunks

        for elem in groupSizes:
            if elem not in seen_array:
                index_array = get_index(groupSizes, elem)
                seen_array.append(elem)
                result.append(split_list(index_array, elem))

        result1 = [x for xs in result for x in xs]
        return result1


groupSizes = [3, 3, 3, 3, 3, 1, 3]
result = Solution()
print(result.groupThePeople(groupSizes))
