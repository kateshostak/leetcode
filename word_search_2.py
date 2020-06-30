from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def traverse(word, i, j, k):
            if k == len(word):
                return True
            if i < 0 or i == len(board):
                return False
            if j < 0 or j == len(board[0]):
                return False
            if word[k] != board[i][j]:
                return False
            tmp = board[i][j]
            board[i][j] = -1
            a = traverse(word, i + 1, j, k + 1)
            b = traverse(word, i, j + 1, k + 1)
            c = traverse(word, i - 1, j, k + 1)
            d = traverse(word, i, j - 1, k + 1)
            board[i][j] = tmp
            return a or b or c or d
        res = []
        for word in words:
            if traverse(word, 0, 0, 0):
                res.append(word)
        return res


def main():
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    res = Solution().findWords(board, words)
    print(f'expected::["eat", "oath"], got::{res}')


if __name__ == '__main__':
    main()
