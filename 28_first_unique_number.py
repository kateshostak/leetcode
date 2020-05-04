from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = []
        self.i = -1
        self.d = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.i < len(self.nums) and self.d[self.nums[self.i]] == 1:
            self.i += 1
            return self.nums[self.i]
        return -1

    def add(self, x: int) -> None:
        self.nums.append(x)
        if x in self.d:
            self.d[x] += 1
        else:
            self.d[x] = 1


def main():
    comms = ["showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
    args = [[], [5], [], [2], [], [3], []]
    res = []
    f = FirstUnique([2, 3, 5])
    # out = [2,null,2,null,3,null,-1]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)

    comms = ["showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
    args = [[], [7], [3], [3], [7], [17], []]
    f = FirstUnique([7, 7, 7, 7, 7, 7])
    # out = [null,-1,null,null,null,null,null,17]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)

    comms = ["showFirstUnique", "add", "showFirstUnique"]
    args = [[], [809], []]
    f = FirstUnique([809])
    # out = [809,null,-1]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)
    print(res)


if __name__ == '__main__':
    main()
