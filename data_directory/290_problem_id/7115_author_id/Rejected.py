from sys import exit
a, b, c = [int(i) for i in input().split()]
for i in range(c + 1):
    if a * i <= c and (c - a * i) % b == 0:
        print(c, a * i, b)
        print("Yes")
        exit(0)
print("No")