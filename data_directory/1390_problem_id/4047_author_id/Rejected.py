import math
n=list(map(int, input().split()))
print(math.ceil((n[0]*n[2])/100)-n[1])