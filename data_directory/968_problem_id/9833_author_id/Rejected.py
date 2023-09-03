def solve(m,d):
    if m==2:
        if d==1:
            return 4
        else:
            return 5
    elif m%2==0:
        if d==6 or d==7:
            return 6
        else:
            return 5
    else:
        if d==7:
            return 6
        else:
            return 5
m,d=input().strip().split(' ')
m,d=(int(m),int(d))
print(solve(m,d))