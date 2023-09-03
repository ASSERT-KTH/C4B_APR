from math import log10
p, d = [int(n) for n in input().split()]


def getLargestWithKNines (p,k):
  p = p + 1
  return p - p % 10**k -1

def main ():
  maxK = int(log10(p)+1)
  for k in range(maxK, 0, -1):
    T = getLargestWithKNines(p,k)
    if p-T <= d and T >= 0:
      print(T)
      return
  print(p)
  return 

main()