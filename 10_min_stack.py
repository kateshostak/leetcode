class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is not None:
            if x <= self.min:
                self.min = x
                self.min_stack.append(x)
        else:
            self.min = x
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.min:
            self.min_stack.pop()
            self.min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    st = MinStack()
    commands = ["push", "push", "push", "getMin", "pop", "top", "getMin"]
    args = [[-2], [0], [-3], [], [], [], []]
    out = [None, None, None, -3, None, 0, -2]

    commands = ["push","push","push","getMin","pop","getMin"]
    args = [[0],[1],[0],[],[],[]]
    out = [None, None, None, None, 0, None, 0]

    res = []
    for com, arg in zip(commands, args):
        res.append(getattr(st, com)(*arg))
        print(f'com::{com}, arg::{arg}, stack::{st.stack}, min::{st.min_stack}')

    print(res)


if __name__ == '__main__':
    main()
