n = int(input())
get = []
x = 1
out = ''
for i in range(1,n):
    x = (x+i)%n
    if i == n-1 :
        out += str(x) 
    else:
        out += str(x) + ' '
print(out)