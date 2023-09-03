# Description of the problem can be found at http://codeforces.com/problemset/problem/832/A

import math

n, k = map(int, input().split())

if math.floor(n / k)&1 == 1:
    print("YES")
else:
    print("NO")