
def SC(st):
    new_s = ''
    st = list(st)
    if len(st) == 0 or len(st) == 1:
        return st
    i = 0
    while i < len(st):
        cnt = 1
        if i == 0:
            new_s += st[i]
            i += 1
            continue
        print(i)
        while st[i] == st[i-1]:
                cnt += 1
                i += 1
        if cnt > 1:
            new_s += str(cnt)
        else:
            new_s += st[i]
        i +=1


    return new_s


# print(SC('aabcccccaaa'))


def compress(chars):
    chars = list(chars)
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return chars


print(compress('aabcccccaaa'))