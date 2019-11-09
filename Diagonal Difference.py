def diagonalDifference(arr):
    # Write your code here
    primary=0
    secondary = 0
    n = len(arr)
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - i - 1]
    return abs(primary - secondary)