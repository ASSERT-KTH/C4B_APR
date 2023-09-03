n=int (input())
print ("I hate",end=' ')
for i in range (1,n+1):
    if i==n:
        print ("it")
    elif i%2==0:
        print ("that I hate",end=' ')
    else:
        print ("that I love",end=' ')