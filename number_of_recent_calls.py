class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr[0] < t - 3000:
            self.arr.pop(0)
        return len(self.arr)


def main():
    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))


if __name__ == '__main__':
    main()
