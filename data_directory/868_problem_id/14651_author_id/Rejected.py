n = input()
n = int(n)

if n==0 :
    print(1)
else :
    a = [0,8,4,2,6]
    
    n = n%4
    print(a[n])