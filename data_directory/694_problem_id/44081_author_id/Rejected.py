import math
import re

a = input()

if a == 'a1' or a == 'h1' or a == 'a8' or a == 'h8':
        print(3)
elif a[1] == '1' or a[1] == '8' or a[0] == 'a' or a[0] == 'h':
    print(4)
else:
    print(8)




# arr = list(map(int, input().split()))
# m = int(input())
# spis = list(map(int, input().split()))
#
# arr1 = sorted(arr, reverse=True)
# a = [n - arr1.index(arr[el - 1]) for el in spis]
# print(' '.join(map(str, a)))