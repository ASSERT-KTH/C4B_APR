l,b = [int(x) for x in input().split()]

n = 0

while True :
    if(l > b):

        break

    elif (l < b):
        n+=1
        l=3*l
        b = 2*b

print(n)