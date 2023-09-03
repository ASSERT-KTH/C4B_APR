n,k = map(int,input().split())
diploma = (n//2) // (k+1)
gram = diploma *k
s = n - gram - diploma
print(diploma,gram,s)