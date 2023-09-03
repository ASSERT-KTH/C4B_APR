n = input()
N = int(n,10)
m=1
while m>0:
    x = int(m*N) +1
    #print ("%d,%d,%s"%(x,m,N*m))
    i=2
    bool = False
    while i*i <= x :
        if(x%i==0):
            print(m)
            bool = True
            break
        i+=1
    if(bool):
        break
    m+=1