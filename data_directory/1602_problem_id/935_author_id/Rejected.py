x,t,a,b,dA,dB = map(int, input().split())
if x==0 or a==x or b==x:
    print ("YES")
    exit()
tempA = a
tempB = b
for i in range(t):
    tempA = a - i*dA
    tempB = b
    for j in range(t):
        tempB = b - j*dB
        if tempA+tempB == x:
            print ("YES")
            exit()
print ("NO")