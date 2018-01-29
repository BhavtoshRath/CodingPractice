# Recursive implementation of Knapsack problem.
#Thoughts: Definitely a unique recursive approach of start from maximum
# and recurse down the list.

def knapSack(val, wt, W, n):
    if (W == 0 or n == 0):
        return 0

    if wt[n-1] > W:
        return knapSack(val, wt, W, n-1)

    else:
        return max(val[n-1] + knapSack(val, wt, W-wt[n-1], n-1),
                   knapSack(val, wt, W, n-1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(val , wt , W , n))