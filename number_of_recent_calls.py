class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        start = t - 3000
        i = len(self.arr) - 1
        res = 0
        while i >= 0 and self.arr[i] >= start:
            res += 1
            i -= 1
        return res


def main():
    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))


if __name__ == '__main__':
    main()
