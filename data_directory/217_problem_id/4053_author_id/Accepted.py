s = lambda x: x * ( x + 1 ) // 2

n = int( input() )
lo, hi = 0, 10 ** 10
while lo != hi:
    mid = ( lo + hi + 1) // 2
    if s(mid) < n: lo = mid
    else: hi = mid - 1
# while s(lo + 1) < n: lo += 1
print(n - s(lo))