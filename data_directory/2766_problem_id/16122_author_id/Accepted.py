from math import ceil
a = list(input())
b1 = len(a)-1
i = 0
a1 = 0
x = 0

while(i<int(len(a)/2)):
    if(x ==2):
        break
    else:
        z1 = a[a1]
        z2 = a[b1]
        if(z1 != z2):
            x+=1
            a1+=1
            b1-=1
        else:
            a1 += 1
            b1 -= 1
        i +=1

if(len(a)%2==0 and (x ==2 or x==0)):
    print("NO")
elif(len(a)%2!=0 and ( x==0)):
    print("YES")
elif(len(a)%2!=0 and ( x==2)):
    print("NO")
else:
    print("YES")