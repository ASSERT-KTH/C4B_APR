n , k =[int(x)for x in input().split(" ")]
a = n // (2*(1+k))
b = a*k 
c = n - (a+b)
print ("%d %d %d"%(a,b,c))