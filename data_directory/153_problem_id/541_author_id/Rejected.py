# Description of the problem can be found at http://codeforces.com/problemset/problem/610/A

n = int(input())

print(max(0, n // 4 - (1 if n % 4 == 0 else 0)))