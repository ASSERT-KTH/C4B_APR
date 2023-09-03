a = input().split()
y = int(a[0])
k = int(a[1])
n = int(a[2])

xl = []
xf = -1
for x in range(1,n-y+1):
    if (x+y)//k >=100000:
        break

    if (x+y)%k == 0:
        xl.append(x)
        xf = x
        break

while xf!=-1:
    xf += k
    if xf+y > n:
        break
    xl.append(xf)

if len(xl)==0:
    print(-1)
else:
    ans = ""
    for k in xl:
        ans+= str(k)+" "
    print(ans)