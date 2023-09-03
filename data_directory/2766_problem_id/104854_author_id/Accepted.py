str=input()
index=int(len(str)/2)
count=0
for i in range(0,index):
    if not str[i]==str[-i-1]:
        count+=1
if count==1:
    print("YES")
elif count==0 and len(str)%2==1:
    print("YES")
else:
    print("NO")