s = list(input())
while True:
    try:
        s.remove(' ')
    except ValueError:
        break
n = int(s[0])
b = int(s[1])
p = int(s[2])
y = n*p
k = 0
def max(m):
    res = 1
    while m>=res:
        res *= 2
    return res/2    
while n>1:
    k += max(n)/2
    n -= max(n)/2

print (int(k*(2*b+1)),y,sep = ' ')