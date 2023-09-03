x,t,a,b,dA,dB = map(int, input().split())
if x==0 or a==x or b==x:
    print ("YES")
    exit()
tempA = a
tempB = b
for i in range(t):
    tempA = a - i*dA
    #print("A", tempA)
    tempB = b
    for j in range(t):
        tempB = b - j*dB
        #print("B", tempB)
        if tempA+tempB == x or tempA == x or tempB == x:
            print ("YES")
            exit()
print ("NO")