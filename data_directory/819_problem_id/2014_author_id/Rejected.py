d_min=0
x=input()
x+="$"
start=0
z=[]
while start!=len(x)-1:
    if x[start] in 'AEIOUY':
        y=x[start]
        start+=1
        while start!=len(x)-1:
            if x[start] not in 'AEIOUY':
                y+=x[start]
                start+=1
            else:
                break
        z.append(y)
        if d_min<len(y):
            d_min=len(y)
    else:
        start+=1
if z==[]:
    print(len(x))
else:
    print(d_min)