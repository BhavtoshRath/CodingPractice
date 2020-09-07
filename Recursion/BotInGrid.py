



def botInGrid(n, c):
    if n == 1 or c == 1:
        return 1
    else:
        return botInGrid(n-1, c) + botInGrid(n, c-1)
print(botInGrid(8, 8))


# No recursion, DP.
def botInGrid_dp(n, c):  # Bottom-up
    M = [[0 for x in range(n)] for y in range(c)]
    for i in range(n):
        M[i][0] = 1
    for j in range(c):
        M[0][j] = 1
    for i in range(1, n):
        for j in range(1, c):
            M[i][j] = M[i-1][j] + M[i][j-1]
    return M[n-1][c-1]


print(botInGrid_dp(8, 8))
