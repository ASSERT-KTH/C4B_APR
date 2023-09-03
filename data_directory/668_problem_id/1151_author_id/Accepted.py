n=int(input())
s1='I hate'
s2='I love'
s=''
for i in range(n):
    if s=='':
        s+=s1
    else:
        if i%2==0:
            s+=' that '+s1
        else:
            s+=' that '+s2
print(s+' it')