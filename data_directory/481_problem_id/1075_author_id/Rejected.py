#@Carbodose

n=int(input())
x=n%7
if x>2:
    x=2
print(2*(n//7),2*(n//7)+x)