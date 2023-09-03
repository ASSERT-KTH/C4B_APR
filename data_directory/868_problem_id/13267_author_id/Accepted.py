import sys

n = int(input())

if n == 0:
    print(1)
    exit()

arr = [6, 8, 4, 2]
print(arr[n % 4])