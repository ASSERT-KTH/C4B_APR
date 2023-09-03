a1,a2 = input().split()
a1,a2 = int(a1),int(a2)
if a1 == a2:
    print(a1+a2-3)
else:
    if abs(a1-a2)%3 == 0:
        print(a1+a2 - 3)
    else:
        print(a1+a2 -2 )