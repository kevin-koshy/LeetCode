from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        num = []
        for length in range(2, n):
            for start in range(n - length):
                num.append(int(sample[start:start + length]))
        print(num)

        ans_slots = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678,
                     6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789,
                     12345678, 23456789, 123456789]
        result = []
        for num in ans_slots:
            if low <= num <= high:
                result.append(num)
        return result


solution = Solution()
low1 = 100
high1 = 300
print(solution.sequentialDigits(low1, high1))
