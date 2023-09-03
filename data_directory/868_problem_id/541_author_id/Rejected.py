# Description of the problem can be found at http://codeforces.com/problemset/problem/742/A

n = int(input())

if (n - 1) % 4 == 0:
    print("8")
if (n - 1) % 4 == 1:
    print("4")
if (n - 1) % 4 == 2:
    print("2")
if (n - 1) % 4 == 3:
    print("6")