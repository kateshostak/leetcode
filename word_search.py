from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, k):
            if k >= len(word):
                return False

            if board[i][j] == '#' or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'

            if i + 1 < len(board) and traverse(i + 1, j, k + 1):
                return True

            if i - 1 >= 0 and traverse(i - 1, j, k + 1):
                return True

            if j + 1 < len(board[0]) and traverse(i, j + 1, k + 1):
                return True

            if j - 1 >= 0 and traverse(i, j - 1, k + 1):
                return True

            board[i][j] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if traverse(i, j, 0):
                        return True
        return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    res = Solution().exist(board, word)
    print(f'expected::True, got::{res}')

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'SEE'
    res = Solution().exist(board, word)
    print(f'expected::True, got::{res}')

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    res = Solution().exist(board, word)
    print(f'expected::False, got::{res}')

    board = [['a', 'b']]
    word = 'ba'
    res = Solution().exist(board, word)
    print(f'expected::True, got::{res}')

    board = [['C', 'A', 'A'], ['A', 'A', 'A'], ['B', 'C', 'D']]
    word = 'AAB'
    res = Solution().exist(board, word)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()
