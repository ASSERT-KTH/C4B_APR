# Description of the problem can be found at http://codeforces.com/problemset/problem/723/A

x1, x2, x3 = map(int, input().split())
a_x = (x1 + x2 + x3) // 3
print(abs(a_x - x1) + abs(a_x - x2) + abs(a_x - x3))