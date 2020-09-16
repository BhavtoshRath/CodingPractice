def magic_index(seq, start = None, end = None):
    if start is None:
        start = 0

    if end is None:
        end = len(seq) - 1

    if start > end:
        return -1

    index = (start + end) // 2
    if index == seq[index]: # array indexing with `[]` not `()`
        print("Equal to index. Value of index = %s" % index) # use % to print index
        return index

    if index > seq[index]:
        print("Greater than loop. Value of Index = %s" % index)
        return magic_index(seq, start=index + 1, end=end)
    else:
        print("Else part of Greater. Value of index = %s" % index)
        return magic_index(seq, start=start, end=index - 1)


result = magic_index(seq=[0, 2, 4, 6], start=None, end=None)
if result == -1:
    print('No Result Found!')


# def magind(seq, start=None, end=None):
#     if start is None:
#         start = 0
#     if end is None:
#         end = len(seq) - 1
#
#     if start > end:
#         return False
#
#     index = (start + end) // 2
#
#     if index == seq[index]:
#         return index
#     elif index > seq[index]:
#         return magind(seq, )


