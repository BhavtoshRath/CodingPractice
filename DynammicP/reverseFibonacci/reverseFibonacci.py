

def reverseFibonacci(n):
    l = [0]*n  # Memoization
    l[0] = 0
    l[1] = 1
    for i in range(2, n):
        l[i] = l[i-1] + l[i-2]

    return ''.join(str(e) for e in l[::-1])


print(reverseFibonacci(4))




# def Fibonacci(n): # No memoization
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

# def Fibonacci(n):
#     l = [0]*n  # Memoization
#     l[0] = 0
#     l[1] = 1
#     for i in range(2, n):
#         l[i]=l[i-1]+l[i-2]
#     return l[n-1]

print(Fibonacci(100))
