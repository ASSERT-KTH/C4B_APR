#!/usr/bin/python3.5
x = int(input())
if x == 1:
    print(1)
    quit()
elif x == 2:
    print(3)
    quit()
elif x == 3:
    print(5)
    quit()
else:
    if x % 2 == 0:
        k = x * 2
    else:
        k = x * 2 - 1

for n in range(1, 16, 2):
    if n ** 2 >= k:
        print(n)
        break