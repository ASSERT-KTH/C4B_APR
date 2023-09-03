# Description of the problem can be found at http://codeforces.com/problemset/problem/579/A

d1, d2, d3 = map(int, input().split())
s = 0

s += d1

if d1 + d2 < d3:
    s += d1 + d2
else:
    s += d3

if d2 < d1 + d3:
    s += d2
else:
    s += d1 + d3
    
print(s)