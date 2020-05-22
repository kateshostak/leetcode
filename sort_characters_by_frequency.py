from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        d = sorted(c, key=lambda x: c[x])
        return ''.join([l*c[l] for l in d[::-1]])



def main():
    s = "tree"
    res = Solution().frequencySort(s)
    print(f'expected::eert, got::{res}')


if __name__ == '__main__':
    main()
