a = int(input())
b = int(input())
i = 0
if a == b:
    print(1)
else:
    while a <= b:
        i += 1
        a *= 3
        b *= 2
        print(a)
        print(b)
        print()
    print(i)