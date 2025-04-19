"""
Given an m x n 2D binary grid "grid" which represents a map of '1's (land) and '0's (water), return the number of
islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""
from collections import deque
from typing import List


# region Solution

def num_islands(grid: List[List[str]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    island_count = 0

    def dfs(row: int, column: int):
        if row >= rows or row < 0 or column >= columns or column < 0 or grid[row][column] == "0":
            return

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid[row][column] = "0"

        for x, y in directions:
            dfs(row + x, column + y)

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "1":
                dfs(i, j)
                island_count += 1

    return island_count


def num_islands_bfs(grid: List[List[str]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    visited_elements = set()
    islands = 0

    def bfs(bfs_row: int, bfs_column: int):
        queue = deque()
        visited_elements.add((bfs_row, bfs_column))
        queue.append((bfs_row, bfs_column))

        while queue:
            popped_element = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for x, y in directions:
                next_row = popped_element[0] + x
                next_column = popped_element[1] + y

                if next_row in range(rows) and next_column in range(columns) and grid[next_row][
                    next_column] == "1" and (next_row, next_column) not in visited_elements:
                    queue.append((next_row, next_column))
                    visited_elements.add((next_row, next_column))

        return None

    for row in range(rows):
        for column in range(columns):
            element = grid[row][column]

            if element == "1" and (row, column) not in visited_elements:
                islands += 1
                bfs(row, column)

    return islands


# endregion

# region Tests

# 1
print(num_islands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]))

# 3
print(num_islands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]))

# endregion
