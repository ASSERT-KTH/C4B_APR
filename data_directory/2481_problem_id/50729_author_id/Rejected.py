friends=["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

n=int(input())

a=n%5

if n>5:
    if a==0:
        print("Howard")

    elif a==4:
        print("Rajesh")

    elif a==3:
        print("Penny")

    elif a==2:
        print("Leonard")

    elif a==1:
        print("Sheldon")

elif n<=5:
    if n==5:
        print("Howard")

    elif n==4:
        print("Rajesh")

    elif n==3:
        print("Penny")

    elif n==2:
        print("Leonard")

    elif n==1:
        print("Sheldon")