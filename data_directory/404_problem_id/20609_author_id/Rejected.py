i=1
line=input()
n=len(line)-1
a=int(line[1])
b=int(line[2])
k=10*a+b
while i<n:
    a=int(line[i])
    b=int(line[i+1])
    if a>0 and b>0:
        p=10*a+b
        if p<=k:
            k=p
    i+=1
print(k)