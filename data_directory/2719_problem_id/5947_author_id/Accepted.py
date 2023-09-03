# A.Bear and Big Brother
a, b = map(int, input().split())
i = 0
while a <= b:
    i += 1
    a = a*3
    b = b*2
    if a > b:
        print(i)
        break