_,t=map(int,input().split())
s=input()
while t>0:
    i=0
    s1=''
    while i<len(s)-1:
        if s[i]=='B'and s[i+1]=='G':
            s1+=s[i+1]+s[i]
            i+=1
        else:
            s1+=s[i]
        i+=1
    if s[len(s)-1]=='B':
        s1+='B'
    s=s1
    t-=1
print(s)
#print(' '.join([str(i) for i in a]))