a1,a2 = input().split()
a1,a2 = int(a1),int(a2)
if a1 == a2 and a1 != 1:
    print(a1+a2-3)
elif a1 ==1 and a2 == 1:
    print(0)
else:
    if abs(a1-a2)%3 == 0:
        print(a1+a2 - 3)
    else:
        print(a1+a2 -2 )