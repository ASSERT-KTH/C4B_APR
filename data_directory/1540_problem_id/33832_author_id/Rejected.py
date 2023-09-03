k=[(i*(i+1))//2 for i in range(1,45001)]
n=int(input())
t = False
for i in k:
    if (n-i) in k:
        print("YES")
        t=True
        break
if t==False:
    print("NO")