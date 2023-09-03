x = raw_input().split()
n = int(x[0])
m = int(x[1])
a = int(x[2])

y = n / a 
if(n % a):
    y+=1

z = m / a
if(m % a):
    z+=1

print(y*z)