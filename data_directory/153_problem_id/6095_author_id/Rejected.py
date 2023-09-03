x=int(input())
i=1
while 1:
    y=x
    y=(y-(2*i))/2
    if y<=i:
        break
    i+=1
i-=1
print(i)