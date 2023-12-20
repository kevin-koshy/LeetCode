class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.repeat_sum(num)
        return num

    def repeat_sum(self,num):
        total = 0;
        while num >= 10:
            num_add = num % 10
            total += num_add
            num = num // 10
        return total + num


result = Solution()
print(result.addDigits(10))
