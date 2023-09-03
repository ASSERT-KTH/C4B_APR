n=int(input())
s=input()
l=[0 for i in range(n)]
r=0
o=0
def odin(k):
    j=1
    d=False
    while not(d) and j<len(k)-1:
        d=k[j]==k[j+1] or k[j]==k[j-1]
        j+=1
    if len(k)==2:
        d=k[j]==k[j-1]
    r=j
    return(d)
for i in range(n):
    l[i]=s[i]
while odin(l):
    del(l[r])
    o+=1
print(o)