class StockSpanner:

    def __init__(self):
        self.prices = []
        self.arr = []
        self.counter = 1

    def next(self, price: int) -> int:
        if self.prices and price >= self.prices[-1]:
            self.counter += 1
        else:
            self.counter = 1
        self.prices.append(price)
        self.arr.append(self.counter)
        j = len(self.prices) - 1
        sum_ = 0
        print(f'prices::{self.prices}')
        print(f'arr::{self.arr}')
        while j >= 0 and self.prices[j] <= price:
            print(f'j::{j}, self.arr[j]::{self.arr[j]}')
            sum_ += self.arr[j]
            j -= self.arr[j]
        return sum_


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
