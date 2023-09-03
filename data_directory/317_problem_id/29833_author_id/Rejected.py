def drive(n,a):
    time = 0
    if a == n:
        return 1
    while time != a and time != n-a:
        time = time + 1
    return time
    
        
    
x,y = map(int,input().split())
print(drive(x,y))