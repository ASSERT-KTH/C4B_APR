def gcd(a,b):
    c=max(a,b)
    while c>0:
        if a%c==0 and b%c==0:
            return c
        elif c>min(a,b):
            c=min(a,b)
            continue
        else:
            c-=1
            continue


inp=[int(i) for i in input().split()]
n=inp[2]
win=0
lose=0
turn=True

while n>=inp[0] and n>=inp[1]:
    if turn==True: #Simon's Turn
        n = n-gcd(inp[0],n)
        win+=1
        turn=False
        continue
    elif turn==False: #Antisimon's Turn
        n = n-gcd(inp[1],n)
        lose+=1
        turn=True
        continue

if win>lose:
    print(0)
else:
    print(1)