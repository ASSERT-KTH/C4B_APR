import sys
n = int(input())
if(n < 5):
    print("0")
else:
    d = int(n/2)
    if(d%2 == 0):
        print((int(d/2))-1)
    else:
        print(int(d/2))