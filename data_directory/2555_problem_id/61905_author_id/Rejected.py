n=input()
count=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count=count+1
if count==7:
    print("YES")
else:
    print("NO")