n=list(input())
temp=''.join(n)
le=len(n)
l=len(n)//2
if (temp==temp[::-1]) and le%2==0:
    print("NO")
    exit()
if temp==temp[::-1] and le%2!=0:
    print("YES")
    exit()
    
if le%2==0:
    n1=n[:l]
    n2=n[l:][::-1]
    c=0
    for i in list(zip(n1,n2)):
        i=list(i)
        if i[0]!=i[1]:
            c=c+1
        if c>1:
            print("NO")
            exit()
    print("YES")
if le%2!=0:
    n1=n[:l]
    n2=n[l+1:][::-1]
    c=0
    for i in list(zip(n1,n2)):
        i=list(i)
        if i[0]!=i[1]:
            c=c+1
        if c>1:
            print("NO")
            exit()
    print("YES")