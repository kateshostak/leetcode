import math


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.alphabet = {i: elem for i, elem in enumerate(characters)}
        self.positions = [0]*combinationLength
        self.notch = len(characters) - 1
        self.length = combinationLength
        self.n = math.factorial(len(characters))//(math.factorial(len(characters) - self.length))
        self.i = 0

    def next(self) -> str:
        comb = ''.join(self.alphabet[i] for i in self.positions)
        self.step()
        self.i += 1
        return comb

    def step(self):
        carry = 0
        if self.positions[-1] + 1 > self.notch:
            carry = 1
        else:
            self.positions[-1] += 1
            return

        for i in range(self.length - 1, -1, -1):
            tmp = self.positions[i] + carry
            if tmp > self.notch:
                carry = 1
                self.positions[i] = 0
            else:
                carry = 0
                self.positions[i] += 1

    def hasNext(self) -> bool:
        return self.i < self.n


def main():
    characters = "abc"
    combinationLength = 2
    obj = CombinationIterator(characters, combinationLength)

    param_1 = obj.next()
    print(param_1)
    param_2 = obj.hasNext()
    print(param_2)

    param_1 = obj.next()
    print(param_1)
    param_2 = obj.hasNext()
    print(param_2)

    param_1 = obj.next()
    print(param_1)
    param_2 = obj.hasNext()
    print(param_2)

if __name__ == '__main__':
    main()
