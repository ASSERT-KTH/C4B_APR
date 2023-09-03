import sys
num = int(input())
left = num % 4

if num == 0:
    print(1)
elif left % 4 == 2:
    print(4)
elif left % 4 == 0:
    print(6)
elif left % 4 == 1:
    print(8)
elif left % 4 == 3:
    print(2)