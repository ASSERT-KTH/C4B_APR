n=int(input())

lucky=[]

b=0
number1=10000000000000000000000000000000000000000000000000000000
while n>b*7:
    a=(n-b*7)//4
    
    
    if ((n-b*7)%4)==0:
        number2=a+b
        if number2<number1:
            number1=number2
            x=a
            y=b
    elif n%7==0:
        number1=(n//7)
        x=0
        y=number1
        
    b+=1


if number1!=10000000000000000000000000000000000000000000000000000000:
    print(x*"4"+y*"7")


else:
    print("-1")