x = int(input())
for i in range(x):
    if(i%2==0):
        print("I hate",end=" ")
    elif(i%2==1):
        print("I love",end=" ")

    if(i == x-1):
        print("it")
    else:
        print("that",end=" ")