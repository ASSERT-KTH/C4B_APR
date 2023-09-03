n = int(input())
a = int(input())
b = int(input())
c = int(input())
ans  = 0
if  a <= b - c:
    ans = n//a
else:
    ans = (n - c)// (b -c)
    rem = c + (n - c ) - (b -c) * ans
    while(rem >= b):
        rem = rem - (b -c)
        ans+=1;
    
    if rem >= a:
        ans += rem//a
    
print(ans)