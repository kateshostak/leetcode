from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def traverse(i, j):
            if i < 0 or i >= len(board):
                return

            if j < 0 or j >= len(board[0]):
                return

            if board[i][j] == 'X' or board[i][j] == '#':
                return

            if board[i][j] == 'O':
                board[i][j] = '#'

            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                traverse(0, j)

        for j in range(len(board[0])):
            if board[len(board) - 1][j] == 'O':
                traverse(len(board) - 1, j)

        for i in range(len(board)):
            if board[i][0] == 'O':
                traverse(i, 0)

        for i in range(len(board)):
            if board[i][len(board[0]) - 1] == 'O':
                traverse(i, len(board[0]) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


def main():
    board = [
            ['X', 'O', 'X', 'X'],
            ['X', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X'],
            ['X', 'X', 'O', 'X']
    ]

    Solution().solve(board)
    for row in board:
        print(*row)

    print()

    board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']
        ]

    Solution().solve(board)
    for row in board:
        print(*row)


if __name__ == '__main__':
    main()
