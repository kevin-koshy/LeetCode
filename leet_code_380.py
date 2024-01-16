from random import choice
class RandomizedSet:

    def __init__(self):
        self.dict_set = {}
        self.seed = 10
        self.count = 10

    def insert(self, val: int) -> bool:
        if val not in self.dict_set:
            self.dict_set[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict_set:
            del self.dict_set[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(list(self.dict_set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(-1)
param_2 = obj.remove(-2)
param_3 = obj.insert(-2)
param_4 = obj.getRandom()
param_5 = obj.remove(-1)
param_6 = obj.insert(-2)
param_7 = obj.getRandom()

print(param_1, param_2, param_3, param_4, param_5, param_6, param_7)
