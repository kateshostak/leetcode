from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        checked_image = []
        for row in image:
            tmp_row = []
            for columnb in row:
                tmp_row.append('*')
            checked_image.append(tmp_row)

        def traverse(r, c):
            if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != color or checked_image[r][c] == '#':
                return
            image[r][c] = newColor
            checked_image[r][c] = '#'
            traverse(r, c + 1)
            traverse(r, c - 1)
            traverse(r + 1, c)
            traverse(r - 1, c)
        traverse(sr, sc)
        return image


def main():
    image = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
    sr = 1
    sc = 1
    newColor = 2
    Solution().floodFill(image, sr, sc, newColor)
    for row in image:
        print(*row)

    image = [
            [0, 0, 0],
            [0, 1, 1]
        ]
    sr = 1
    sc = 1
    newColor = 1
    Solution().floodFill(image, sr, sc, newColor)
    for row in image:
        print(*row)


if __name__ == '__main__':
    main()
