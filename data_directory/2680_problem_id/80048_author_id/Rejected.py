import time
n, *arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

time.sleep(1)
print(' '.join(list(map(str, arr))))