#!/usr/bin/python3

def readln(): return tuple(map(int, input().split()))

n, = readln()
a = [readln() for _ in range(n)]
m = (n + 1) // 2
print(sum([a[i][i] + a[i][n - i - 1] + a[m][i] + a[i][m] for i in range(n)]) - 3 * a[m][m])