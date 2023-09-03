n=int(input())
j=0
s=str(n)
k=len(s)
l=int(n/4)
m=int(n/7)
for i in range(k):
    #print(s[i])
    if(s[i]==0):
        break
    elif((int(s[i])/4==1)or(int(s[i])/7==1)):
        j=j+1
    elif((n==l*l) or (n==m*m)):
        j=j+1
#print(j)
if(j==0):
    print("NO")
elif(j==k):
    print("YES")
else:
    print("NO")