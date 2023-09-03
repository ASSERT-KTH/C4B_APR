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
        if i<=int(n/2):
            a+=1
        else:
            b+=1
else:
    if a==b:
        print("YES")
    else:
        print("NO")