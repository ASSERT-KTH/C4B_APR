def Prime(x):
    if x<2: return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True
n=int(input())
if Prime(n): print(1)
elif n%2==0 or Prime(n-2): print(2)
else: print(3)