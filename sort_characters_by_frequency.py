from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        bucket = [-1]*(len(s) + 1)
        for l, freq in c.items():
            if bucket[freq] == -1:
                bucket[freq] = []
            bucket[freq].append(l)

        new_s = ''
        for i in range(len(s) - 1, -1, -1):
            if bucket[i] != -1:
                for l in bucket[i]:
                    new_s += l*i

        return new_s


def main():
    s = "tree"
    res = Solution().frequencySort(s)
    print(f'expected::eert, got::{res}')


if __name__ == '__main__':
    main()
