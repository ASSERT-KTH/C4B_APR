import re

s = input()

is_seven = re.search(r'1{7}|0{7}', s)

if is_seven is None:
    print('NO')
else:
    print('YES')