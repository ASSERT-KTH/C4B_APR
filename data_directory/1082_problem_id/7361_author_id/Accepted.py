import math
k,l  = [int(input()) for i in range(2)]
i=math.floor(math.log(l,k)+0.5)
print('NO' if l!=(k**i) else 'YES\n'+str(i-1))