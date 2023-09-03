st = input()
number = 0
for c in st:
    if c == '4' or c == '7':
        number += 1
if number == 4 or number == 7:
    print("YES")
else:
    print("NO")