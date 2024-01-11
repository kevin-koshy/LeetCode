class Logger:

    def __init__(self):
        self.time_stamp = -1
        self.message = ""
        self.time_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.time_dict and self.time_dict[message] + 10 > timestamp:
            return False
        else:
            self.time_dict[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
obj = Logger()
param_1 = obj.shouldPrintMessage(1, "foo")
param_2 = obj.shouldPrintMessage(2, "bar")
param_3 = obj.shouldPrintMessage(3, "foo")
param_4 = obj.shouldPrintMessage(8, "bar")
param_5 = obj.shouldPrintMessage(10, "foo")
param_6 = obj.shouldPrintMessage(11, "foo")

print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
print(param_6)
