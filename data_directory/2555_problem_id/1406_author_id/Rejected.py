n=str(input())
l=len(n)
p=0
for i in range(0,l-7):
    if n[i]==n[i+1]==n[i+2]==n[i+3]==n[i+4]==n[i+5]==n[i+6]:
        p=p+1
    else:
        continue
if p>=1:
    print("YES")
else:
    print("NO")