n=int(input())
s=""
while (n>=6):
    s+="9"
    n-=6
if n==5:
    s+="7"
    s+="1"
elif n==4:
    s+="7"
elif n==3:
    s+="7"
elif n==2:
    s+="1"

print(int(s))