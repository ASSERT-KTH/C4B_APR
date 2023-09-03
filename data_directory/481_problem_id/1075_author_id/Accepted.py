n=int(input())
x=n%7
y=0
if x==6:
    y=1
if x>2:
    x=2
print(2*(n//7)+y,2*(n//7)+x)

#@Carbodose