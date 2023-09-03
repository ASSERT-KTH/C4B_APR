x = input().split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

i = 0
z = 0
if(c < a):
    print('0')
else:
    while(0<=c):
        i += 1  
        if(i%2==1):
            if(c%a==0):
                c -= a  
            else:
                c -= 1
        else:
            if(c%b==0):
                c -= b
            else:
                c -= 1
    print(i%2)