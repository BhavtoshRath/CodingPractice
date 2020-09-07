# def insert(bin1, bin2, i):
#     bin1 = list(bin1)
#     bin2 = list(bin2)
#     if (len(bin1) - i) != len(bin2):
#         return False
#     else:
#         for ind in range(i, i + len(bin2)):
#             if bin1[ind] == '0' and bin2[ind - 6] == '0':
#                 bin1[ind] = '0'
#             elif bin1[ind] == '0' and bin2[ind - 6] == '1':
#                 bin1[ind] = '1'
#             elif bin1[ind] == '1' and bin2[ind - 6] == '0':
#                 bin1[ind] = '1'
#             else:
#                 while bin2
#     return bin1
#
#
# print(insert('10100000000', '10011', 6))


def updateBits(n, m, i, j):
    # Create a mask to clear bits i through
    # j in n. EXAMPLE: i = 2, j = 4. Result
    # should be 11100011. For simplicity,
    # we'll use just 8 bits for the example.

    # will equal sequence of all ls
    allOnes = ~0

    # ls before position j,
    # then 0s. left = 11100000
    left = allOnes << (j + 1)

    # l's after position i. right = 00000011
    right = ((1 << i) - 1)

    # All ls, except for 0s between
    # i and j. mask 11100011
    mask = left | right

    # Clear bits j through i then put min there
    n_cleared = n & mask

    # Move m into correct position.
    m_shifted = m << i

    return (n_cleared | m_shifted)


# Driver Code
n = 1024  # in Binary N = 10000000000
m = 19  # in Binary M = 10011
i = 2;
j = 6
print(updateBits(n, m, i, j))