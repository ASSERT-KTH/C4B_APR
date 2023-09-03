inp = int(input())
d = 1

for i in range(0, inp-1):
    d += i + 1
    print(d%inp, end=" ")