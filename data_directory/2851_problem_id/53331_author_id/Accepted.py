a, b = list(map(int, input().split()))
d1 = int(a**0.5)
d2 = int(((1+4*b)**0.5 - 1)/2)
if d1>d2:
    print("Valera")
else:
    print("Vladik")