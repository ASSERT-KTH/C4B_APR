from sys import stdin
t,s,x = map(int,stdin.readline().split())
res = t+s+1
if(t == x or t+s == x or t+s+1 == x):
    print("YES")
elif(t == 0 and s == 0 and x == 2):
    print("NO")
else:
    if(x < t+s+1):
        print("NO")
    else:
        if((x -(t+s+1)) % s == 0):
            print("YES")
        else:
            a = (x -(t+s+1) )% s
            if(s-a == 1):
                print("YES")
            else:
                print("NO")