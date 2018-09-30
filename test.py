import sys

s = input('Enter number: ')
# s = 114114
# s = str(s)
if int(s) >1 and int(s) <= 10**9:
    l = ['144', '14', '1']
    for mn in l:
        if mn in s:
            s = s.replace(mn, '')
        if len(s) == 0:
            print('YES')
        else:
            print('NO')
else:
    print('Invalid No.')


