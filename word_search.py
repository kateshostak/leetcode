from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, k):
            if board[i][j] == '#':
                return True
            if board[i][j] != word[k]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'
            if k + 1 < len(word):
                if i + 1 < len(board):
                    if not traverse(i + 1, j, k + 1):
                        return False

                if i - 1 > 0:
                    if not traverse(i - 1, j, k + 1):
                        return False

                if j + 1 < len(board[0]):
                    if not traverse(i, j + 1, k + 1):
                        return False

                if j - 1 > 0:
                    if not traverse(i, j - 1, k + 1):
                        return False
            board[i][j] = tmp
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if not traverse(i, j, 0):
                        return False
        return True


def main():
    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = 'ABCCED'
    res = Solution().exist(board, word)
    print(f'expected::True, got::{res}')


