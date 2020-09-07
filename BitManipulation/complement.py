def onestwos(bin):
    s1 = ''
    for i in bin:
        if i == '0':
            s1 += '1'
        else:
            s1 += '0'

    s2_l = list(s1)
    # Break after first occurrence of '0'.
    for i in reversed(range(len(s1))):
        if s1[i] == '1':
            s2_l[i] = '0'
        else:
            s2_l[i] = '1'
            break

    i -= 1
    if i == -1:
        s2 = ''.join(s2_l)
        s2 = '1'+ s2
    else:
        s2 = ''.join(s2_l)

    return s1, s2


print(onestwos('0000'))