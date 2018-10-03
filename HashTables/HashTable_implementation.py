def hash(astring, tablesize):
    sum = 0
    for char in astring:
        sum += ord(char)

    return sum%tablesize

hash('rath', 7)