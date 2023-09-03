import math
prime = [2]
def isPrime(arg):
    flag = True
    for i in range(3,arg+1):
        for j in range(2,i//2+1):
            if i%j == 0: 
                flag = False
                break
        if flag: prime.append(i)
        flag = True
n,k = map(int,input().split())
isPrime(n)
#print(prime)
count = 0
for i in range(len(prime)):
    #print(prime[i])
    for j in range(len(prime)-1):
        #print(prime[j],prime[j+1],count)
        if prime[j]+prime[j+1]+1 == prime[i]: 
            count+=1
if count == k: 
    print("YES")
else: print("NO")