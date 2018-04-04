
def newmanConway(n):
    p = [0]*(n+1)  # Memoization
    p[0] = 1
    p[1] = 1
    p[2] = 1
    for i in range(3, n+1):
        p[i] = p[p[i-1]] + p[i - p[i-1]]
        # print(p[i])

    return p[n]


print(newmanConway(10))



