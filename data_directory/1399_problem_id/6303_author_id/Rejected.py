def pri(n):
    f = 0
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            f = 1
            break
    return f
    

def nol(n):
    n = n-1
    f = 0
    for i in range(2,n//2):
        if pri(i) == 0 and pri(n-i) == 0 and i != n-i:
            c = 0
            for i in range(i+1,n-i):
                if pri(i) == 0:
                    c = 1
            if c == 0:
                f = 1 
                return "YES"
                break
            else:
                continue
        if f == 1:
            break
        else:
            continue




x,y = input().split()
x = int(x)
y = int(y)
c = 0
for i in range(2,x+1):
    if pri(i) == 0 and nol(i) == "YES":
        c += 1
if c < y:
    print ("NO")
else:
    print ("YES")