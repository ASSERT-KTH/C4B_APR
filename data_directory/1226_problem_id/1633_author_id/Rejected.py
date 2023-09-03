n = int(input())
string = input()
pages = list(map(int, string.split()))
d = 0
a = 0
while a < n:
    a += pages[d % 7]
    d += 1
print(d % 7)