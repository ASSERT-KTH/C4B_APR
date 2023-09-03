str=input().split()
a=int(str[0])
b=int(str[1])
count=0
if a==b:
    print("1")
else:
    while(a<b):
        a=a*3
        b=b*2
        count+=1

    print(count)