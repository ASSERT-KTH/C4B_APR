import sys,re, array, math,functools
input = lambda:sys.stdin.readline()
@functools.lru_cache(maxsize = 10000000)

def Main():
  a, b = map(int, input().split())
  cnt = 0
  sm = 0
  
  while a <= b:
    cnt += 1
    a , b = a*3, b*2
  print(cnt)
if __name__ == '__main__':
  Main()