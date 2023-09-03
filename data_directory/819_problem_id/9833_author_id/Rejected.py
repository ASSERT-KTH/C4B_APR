s=str(input())
list1=['A','E','I','O','U']
m=0
c=-100000
for i in range(len(s)):
    if s[i] in list1:
        if c<0:
            c=i
            m=i+1
        else:
            if i-c>m:
                m=i-c
                #print(i-c,m)
            c=i
if c==-100000:
    print(len(s)+1)
else:
    print(max(m,len(s)-1-c))