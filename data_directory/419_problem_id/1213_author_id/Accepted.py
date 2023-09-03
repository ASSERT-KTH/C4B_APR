n,a,b = input().split()
n,a,b = int(n),int(a),int(b)
if b>0:
    Sum = a +b%n
    if Sum >n:
        Sum = Sum - n 
    print(Sum)
elif b<0:
    Sum = a - abs(b)%n
    if Sum <=0:
        Sum = Sum +n
    print(Sum)
elif b == 0:
    print(a)