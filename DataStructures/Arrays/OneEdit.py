s1 = 'geeks'
s2 = 'geek'

def OneEdit(s1, s2):
    edits = 0
    if s1 == s2:
        return 0
    if abs(len(s1) - len(s2)) > 1:
        return False
    s = min(len(s1), len(s2))
    for i in range(s):
        if s1[i] == s2[i]:
            continue
        else:
            if len(s1) == len(s2):
                s1[i] = s2[i]  # update
                edits += 1
            elif len(s1) > len(s2):
                s1.remove(s1[i])
                edits += 1
            else:
                s2.remove(s2[i])
                edits += 1
        i += 1

    if edits > 1:
        return False
    else:
        return True


OneEdit(s1, s2)



