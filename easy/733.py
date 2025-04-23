"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel
value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill
on the image starting from the pixel image[sr][sc].

To perform a flood fill:
1. Begin with the starting pixel and change it's color to color.
2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the
   original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color
   if it matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.
"""
from typing import List


# region Solution

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows = len(image)
    columns = len(image[0])
    original_color = image[sr][sc]

    if color == original_color:
        return image

    def dfs(row: int, column: int):
        if row < 0 or row >= rows or column < 0 or column >= columns or image[row][column] != original_color:
            return

        image[row][column] = color

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for x, y in directions:
            dfs(row + x, column + y)

    dfs(sr, sc)
    return image


# endregion

# region Tests

# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

# endregion
