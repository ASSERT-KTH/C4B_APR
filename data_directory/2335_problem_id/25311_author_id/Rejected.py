import re

s = input()

success = re.search(r'h.+e.+l.+l.+o', s)

if success is None:
    print('NO')
else:
    print('YES')