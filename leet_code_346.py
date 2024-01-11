class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.result = []

    def next(self, val: int) -> float:
        self.result.append(val)
        return (sum(self.result[-self.size:]))/min(len(self.result), self.size)

    def print_avg(self):
        print(self.result)

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
print(param_1)
param_2 = obj.next(10)
print(param_2)
param_3 = obj.next(3)
print(param_3)
param_4 = obj.next(5)
print(param_4)
