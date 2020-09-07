

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# print(fib(10))

# F = [False] * 50  # Array to store fibonacci terms
#
#
# def fibonacci_top_down(n):
#     if F[n] is False:
#         if n == 0:
#             F[n] = 0
#         elif n == 1:
#             F[n] = 1
#         else:
#             F[n] = fibonacci_top_down(n-1) + fibonacci_top_down(n-2)
#     return F[n]
#
#
# print(fibonacci_top_down(10))


F = [False] * 50  # Array to store fibonacci terms


def fibonacci_bottom_up(n):
    F[n] = 0
    F[1] = 1

    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


print(fibonacci_bottom_up(10))



