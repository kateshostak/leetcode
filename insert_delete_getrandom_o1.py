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
        return True

    def remove(self, val: int) -> bool:
        if val == 2:
            pdb.set_trace()
        if val in self.d:
            i = self.d[val]
            self.arr[i] = self.arr[-1]
            v = self.arr[-1]
            self.d[v] = i
            self.d.pop(val)
            self.arr.pop(-1)
            return True
        return False

    def getRandom(self) -> int:
        print(self.arr)
        return(self.arr[random.randint(0, len(self.arr) - 1)])


def main():
    comms = ["insert", "insert", "remove", "insert", "remove", "getRandom"]
    args = [[0], [1], [0], [2], [1], []]
    sol = RandomizedSet()
    res = []
    for comm, arg in zip(comms, args):
        res.append(getattr(sol, comm)(*arg))

    print(f'expected::[null, true, true, true, true, true, 2], got::{res}')


if __name__ == '__main__':
    main()
