import random


class RandomizedSet:
    def __init__(self):
        self.d = {}
        self.arr = []
        self.len_ = 0

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.arr.append(val)
        self.d[val] = len(self.arr) - 1
        self.len_ = len(self.arr)
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            i = self.d[val]
            self.arr[i] = self.arr[-1]
            self.d.pop(val)
            self.len_ -= 1
            return True
        return False

    def getRandom(self) -> int:
        return(self.arr[random.randint(0, self.len_)])
