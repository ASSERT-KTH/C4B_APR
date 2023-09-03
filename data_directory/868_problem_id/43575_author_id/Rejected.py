import sys
string = input()

num = int(string[-1])

if string == '0':
    print(1)
elif num % 4 == 2 or string == '10':
    print(4)
elif num % 4 == 0:
    print(6)
elif num % 4 == 1:
    print(8)
elif num % 4 == 3:
    print(2)