# l = [7,2,6,4,34,5,7,2,3,1,1,4,69]
l = [38, 27, 43, 3, 9, 82, 10]


def Merge(l):
    if len(l) > 1:
        mid = int((len(l)+1)/2)
        L = l[:mid]
        R = l[mid:]

        Merge(L)
        Merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1

            else:
                l[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1

    return l


print(Merge(l))