import re

s1 = 'ajsb'
print(sorted(s1))

s2 = 'sabj'
print(sorted(s2))

s3 = 'haryy potter    3'
print(s3)

s3_new = re.split(' ', s3).remove('')
print(re.split(' ', s3).remove(''))