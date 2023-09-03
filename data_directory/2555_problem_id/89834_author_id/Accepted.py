import re

str = input()
if len(str) < 7:
    print ('NO')
    exit()

res0 = re.search(r'0000000', str)
res1 = re.search(r'1111111', str)

if res0 != None or res1 != None:
    print ('YES')
else:
    print ('NO')