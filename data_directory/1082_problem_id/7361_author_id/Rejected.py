import math
k,l  = [int(input()) for i in range(2)]
i = math.ceil(math.log(l,k))
print('NO' if l!=(k**i) else 'YES\n'+str(i-1))