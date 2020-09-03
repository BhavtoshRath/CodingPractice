l = [7,2,6,4,34,5,7,2,3,1,1,4,69]
# l = [7,2,6,4]


'''two for loops, use flag, 2nd loop range: (len_l - i - 1)'''
def bubble(l):
    len_l = len(l)
    for i in range(len_l):
        flag_s = True
        for j in range(len_l-i-1):
            # print(i, j)
            if l[j] > l[j+1]:
                temp1 = l[j]
                l[j] = l[j+1]
                l[j+1] = temp1
                flag_s = False

        if flag_s:
            break

    return l


print(bubble(l))

#
# def bubble_sort(array):  # Have flag!!!!!
#     n = len(array)
#
#     for i in range(n):
#         already_sorted = True
#         for j in range(n - i - 1): # n - i - 1 imp!!
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 already_sorted = False
#
#         if already_sorted:
#             break
#
#     return array
#
# print(bubble_sort(l))