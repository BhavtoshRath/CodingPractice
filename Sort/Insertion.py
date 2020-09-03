l = [7,2,6,4,34,5,7,2,3,1,1,4,69]
# l = [7,2,6,4]

def Insertion(l):
    for i in (range(1, len(l))):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
            l[j + 1] = key

    return l

# print(Insertion(l))


def Ins(l):
    for i in range(1, len(l)):
        j = i
        while j != 0:
            if l[i] < l[j-1]:
                temp = l[j-1]
                l[j-1] = l[i]
                l[i] = temp
            j -= 1

    return l

print(Ins(l))

print(7//2)