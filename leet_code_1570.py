from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     for i in range(len(self.nums)):
    #         return 100 + self.nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        def create_sparse_dict(vec):
            # print(vec.nums)
            sparse_dict = {}
            for index, elem in enumerate(vec.nums):
                if elem:
                    sparse_dict[index] = elem
            print(sparse_dict)
            return sparse_dict

        d1 = create_sparse_dict(self)
        d2 = create_sparse_dict(vec)

        sum = 0
        for key in d1:
            if key in d2:
                sum += d1[key]*d2[key]

        return sum

# Your SparseVector object will be instantiated and called as such:
nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)

print(ans)
