# Description of the problem can be found at http://codeforces.com/problemset/problem/761/A

a, b = map(int, input().split())

if abs(a - b) <= 1:
    print("YES")
else:
    print("NO")