a=list(map(int, input().strip.split(' ')))
x=int(abs(a[1]-a[0])/2)
if(a[0]<a[1]):
    min=a[0]
else:
    min=a[1]
print(min, x)