arr = [2, 3, 4, 10, 40]
x = 40

def binary_search(arr, start, end, item):
    l = end - start + 1
    if l % 2 == 0:
        mid_p = int(l/2)
    else:
        mid_p = int((l - 1) / 2)

    #Base case
    if arr[mid_p] == item:
        print(mid_p)
        exit()

    if item >= arr[mid_p]:
        binary_search(arr, mid_p, len(arr) - 1, item)
    else:
        binary_search(arr, 0, mid_p, item)


binary_search(arr, 0, len(arr) -1, x)
