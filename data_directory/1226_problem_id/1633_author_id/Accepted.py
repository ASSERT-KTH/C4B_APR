n = int(input())
string = input()
pages = list(map(int, string.split()))
d = 0
a = 0
while a < n:
    a += pages[d % 7]
    d += 1
e = d % 7
if e == 0:
    e = 7
print(e)