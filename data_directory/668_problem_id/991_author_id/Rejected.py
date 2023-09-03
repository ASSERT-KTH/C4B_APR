a=int(input())
b=["I love that ","I hate that "]
d=[]
c=""
i=1
while i<a:
    d.append(b[(i-1)%2])
    i+=1
l=0
while l<len(d):
    c+=d[len(d)-1-l]
    l+=1
print(d)
print(c+"I hate it")