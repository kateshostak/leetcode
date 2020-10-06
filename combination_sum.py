class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(target, tmp, k):
            if target < 0:
                return False

            if target == 0:
                self.res.append(tmp[:])
                return True

            else:
                for i in range(k, len(candidates)):
                    curr = candidates[i]
                    tmp.append(curr)
                    backtrack(target - curr, tmp, i)
                    tmp.pop()

        self.res = []
        tmp = []
        backtrack(target, tmp, 0)
        return self.res


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    res = Solution().combinationSum(candidates, target)
    print(f'expected::[[2, 2, 3], [7]], got::{res}')


    candidates = [2, 3, 5]
    target = 8
    res = Solution().combinationSum(candidates, target)
    print(f'expected::[[2, 2, 2, 2], [2, 3, 3], [3, 5]] got::{res}')

    candidates = [2]
    target = 1
    res = Solution().combinationSum(candidates, target)
    print(f'expected::[], got::{res}')


if __name__ == '__main__':
    main()
