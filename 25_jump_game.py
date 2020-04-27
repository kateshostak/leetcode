from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        cache = dict()

        def traverse(i):
            if i == 0:
                return True

            for j in range(i-1, -1, -1):
                if i - j <= nums[j]:
                    if j in cache:
                        if cache[j]:
                            return True
                        continue

                    cache[j] = traverse(j)
                    if cache[j]:
                        return True

            cache[i] = False
            return False

        return traverse(len(nums)-1)


def main():
    arr = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    print("got:", Solution().canJump(arr), "want: true")

    arr = [0, 2, 3]
    print("got:", Solution().canJump(arr), "want: false")

    arr = [2, 3, 1, 1, 4]
    print("got:", Solution().canJump(arr), "want: true")

    arr = [3, 2, 1, 0, 4]
    print("got:", Solution().canJump(arr), "want: false")

    arr = [2, 0]
    print("got:", Solution().canJump(arr), "want: true")

    with open("arr.txt", "r") as f:
        import json
        arr = json.loads(f.read())
    print("got:", Solution().canJump(arr), "want: ?")

    with open("arr.txt", "r") as f:
        import json
        arr = json.loads(f.read())
    print("got:", Solution().canJump(list(reversed(arr))), "want: ?")


if __name__ == '__main__':
    main()
