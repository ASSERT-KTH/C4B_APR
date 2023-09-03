n = input()
m=1
while m>0:
    x = int(m*n) +1
    #print (x)
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