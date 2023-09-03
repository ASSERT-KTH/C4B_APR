import sys

def bins(arr, key):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if(key > arr[mid]):
            lo = mid + 1
        else:
            hi = mid

    return hi

n, k = map(int, sys.stdin.readline().split())
tasks = [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]

print(min(bins(tasks, ((240 - k) // 5) * 5) + 1, n))