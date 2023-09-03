n = int(input())
s = str(input())
a = 0
b = 0

for i, num in enumerate(s):
    if num != '7' and num != '4':
        print("NO")
        a=-1
        b=-2
        break
    else:
        if i+1<=n/2:
            a+=int(num)
        else:
            b+=int(num)
else:
    if a==b:
        print("YES")
    else:
        print("NO")