def f(x):
    while True:
        d=x%10
        if d>0: break
        x//=10
    if x<10:
        return True
    else:
        return False
n=int(input())
k=1
while True:
    n+=1
    if f(n): break
    k+=1
print(k)