import numpy as np

grid = [[0, 0, 0, 0, 1, 0, 0, 2, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 5, 0, 6, 0],
        [0, 0, 3, 0, 0, 4, 0, 5, 7],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [6, 4, 0, 9, 0, 0, 1, 0, 0],
        [0, 9, 0, 7, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 6, 0, 0, 0, 3],
        [0, 8, 0, 0, 4, 0, 0, 0, 0]]

solvedSudoku = np.zeros([9, 9], dtype=int)

def possible(y, x, n):
    # checks row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # checks column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # checks 3x3 grid within
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for i in range(9):
        for j in range(9):
            solvedSudoku[i][j] = grid[i][j]

solve()
print(solvedSudoku)
