s=input()
i=0
j=0
x="hello"
while i<len(s) :
    if s[i]!=x[j] :
        i+=1
    if s[i]==x[j] :
        j+=1
        i+=1
    if j==5 :
        print("YES")
        break
    if i==len(s) :
        print("NO")
        break