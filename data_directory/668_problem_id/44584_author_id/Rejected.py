n=int(input())
a=""
if(n==1):
    print("I hate it")
elif(n==2):
    print("I hate that I love it")
else:
    if(n%2==0):
        for i in range ( 1 , n//2):
            a=a+"I hate that I love that"
        b=a+" I hate that I love it"
    else:
        for j in range ( 1 , n//2+1):
            a=a+"I hate that I love that"
        b=a+" I hate it"
    print(b)