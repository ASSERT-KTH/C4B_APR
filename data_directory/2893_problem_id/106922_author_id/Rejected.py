n,k = map(int,input().split())
s = n//2
award = n - s
gram = award// (k + 1) *k
diploma = gram // k
s += award - gram - diploma
print(diploma,gram,s)