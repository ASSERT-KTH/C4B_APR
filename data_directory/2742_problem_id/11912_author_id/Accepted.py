n=int(input())
s=""
if n%2==0:
    s+= n//2 *"1"
else:
    s+= "7"
    s+= (n-3)//2 *"1"
print(int(s))