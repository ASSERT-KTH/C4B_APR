import sys,re, array, math,functools
input = lambda:sys.stdin.readline()
@functools.lru_cache(maxsize = 10000000)

def Main():
  a, b = map(int, input().split())
  # ans =math.ceil( b/a )
  # print(ans)
  if a == b:
    print(1)
    return 0
  cnt  = 0
  sm = 0
  while True:
    sm += a
    cnt += 1
    if sm > b:
      break
  print(cnt)
if __name__ == '__main__':
  Main()