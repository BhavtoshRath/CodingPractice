# https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/

def powerSet(str1, index, curr):
    n = len(str1)

    if (index == n):
        return

    print(curr)

    for i in range(index + 1, n):
        curr += str1[i]
        powerSet(str1, i, curr)
        curr = curr.replace(curr[len(curr) - 1], "")


powerSet('abc', -1, "")


# In recusion function.....
# Index increments by i
# curr string gets appended

