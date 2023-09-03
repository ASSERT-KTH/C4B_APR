n = int(input())
s0 = 0
for i in range(2,n+1):
    s0 = pow(3,i-1)-s0
print(s0%1000000007)