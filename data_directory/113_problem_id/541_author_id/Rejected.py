# Description of the problem can be found at http://codeforces.com/problemset/problem/602/A

def ic(l_c):
    for i in range(len(l_c)):
        if int(l_c[i]) >= 10:
            l_c[i] = chr(int(l_c[i]) - 10 + ord("A"))
    return l_c

l_n = list()

for _ in range(2):
    n, b = map(int, input().split())
    l_n.append(int("".join(ic(input().split())), b))

if l_n[0] < l_n[1]:
    print("<")
elif l_n[1] < l_n[0]:
    print(">")
else:
    print("=")