import math

inp = input().split()
n = eval(inp[0])
t = eval(inp[1])
s = list(input())

def swap(s):
    flag = False
    for i in range(n-2, -1, -1):
        if flag:
            flag = False
            continue
        if s[i] == 'B' and s[i+1] == 'G':
            flag = True
            s[i] = 'G'
            s[i+1] = 'B'
    return s

for i in range(t):
    s = swap(s)
print(''.join(s))