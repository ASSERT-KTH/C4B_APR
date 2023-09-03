a=input()
b="hello"
p=0
for i in range(len(a)):
    if a[i]==b[p]:
        p+=1
    if p==4 :
        print("YES")
        break
if p!=4 : print("NO")