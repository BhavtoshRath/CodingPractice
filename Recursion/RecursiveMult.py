# https://stackoverflow.com/questions/32668423/multiplication-function-with-recursion-in-python

def mult(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        if a < 0 and b > 0:
            return a + mult(a, b - 1)
        elif a < 0 and b < 0:
            return -b + mult(-a - 1, -b) # Imp case: both -ve
        else:
            return b + mult(a - 1, b)


# print(mult(5, 3))
# print(mult(6, -3))
# print(mult(-3, 3))
# print(mult(-3, -33))

print(mult(-3, -2))