def gridGame(grid, k, rules):

    firstGrid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    for i in range(k):
        otherGrid = [[firstGrid[i][j] for j in range(len(firstGrid[i]))] for i in range(len(firstGrid))]
        for row in range(len(otherGrid)):
            for col in range(len(otherGrid[row])):
                aliveNeighbors = countAliveNeighbors(firstGrid, row, col)
                if rules[aliveNeighbors] == "alive":
                    otherGrid[row][col] = 1
                else:
                    otherGrid[row][col] = 0
        firstGrid = [[otherGrid[i][j] for j in range(len(otherGrid[i]))] for i in range(len(otherGrid))]
    return firstGrid


def countAliveNeighbors(grid, row, col):
    count = 0
    if ((row - 1) >= 0):
        if (((col - 1) >= 0) and (grid[row - 1][col - 1] == 1)):
            count += 1
        if (grid[row - 1][col] == 1):
            count += 1
        if ((col + 1) < len(grid[row])) and (grid[row - 1][col + 1] == 1):
            count += 1
    if ((col - 1) >= 0 and (grid[row][col - 1] == 1)):
        count += 1
    if ((col + 1) < len(grid[row]) and grid[row][col + 1] == 1):
        count += 1
    if ((row + 1) < len(grid)):
        if (((col - 1) >= 0) and (grid[row + 1][col - 1] == 1)):
            count += 1
        if (grid[row + 1][col] == 1):
            count += 1
        if ((col + 1) < len(grid[row])) and (grid[row + 1][col + 1] == 1):
            count += 1
    return count   