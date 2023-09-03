p=str(input())
for i in range(0,len(p)):
    if p[i]=='H' or p[i]=='Q' or p[i]=='9' or p[i]=='+':
        print("YES")
        break
else:
    print("NO")