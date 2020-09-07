# if n = x, cover base case till x -1

mem = [False] * 50

def tripleStep(n):
    if mem[n] is not True:
        if n == 0 or n == 1:
            mem[0] = 1
        elif n == 2:
            mem[1] = 1
        else:
            mem[n] = tripleStep(n-2) + tripleStep(n-1)
    return mem[n]

print(tripleStep(20))