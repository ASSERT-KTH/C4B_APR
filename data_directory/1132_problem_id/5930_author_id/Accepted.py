n=int(input())
s=list(str(n))
c=0
for i in range(len(s)):
    if(s[i]=='4' or s[i]=='7'):
        c=c+1
    
if(n%4==0 or n%7==0 or n%47==0):
    print("YES")
elif(c==len(s)):
    print("YES")
else:
    print("NO")