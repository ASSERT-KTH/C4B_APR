a, b = input().split()
a=int(a)
b=int(b)
if a>b:
    if a-b<=1:
        print("YES")
    else:
        print("NO")
else:
    if b-a<=1:
        print("YES")
    else:
        print("NO")