class StockSpanner:

    def __init__(self):
        self.prices = []
        self.arr = []

    def next(self, price: int) -> int:
        counter = 1
        while self.prices and self.prices[-1] <= price:
            counter += self.arr.pop()
            self.prices.pop()
        self.prices.append(price)
        self.arr.append(counter)
        return counter


def main():
    args = [[100], [80], [60], [70], [60], [75], [85]]
    solution = StockSpanner()
    res = []
    for elem in args:
        res.append(solution.next(elem))
    print(res)


if __name__ == '__main__':
    main()
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
