# Description of the problem can be found at http://codeforces.com/problemset/problem/139/A

p = int(input())

l_n = list(map(int, input().split()))
n_s = sum(l_n)

p -= (max(0, p // n_s - 1)) * n_s

for i in range(len(l_n)):
    if l_n[i] >= p:
        print(i + 1)
        quit()
    p -= l_n[i]