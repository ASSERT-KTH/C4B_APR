import sys

size = int(sys.stdin.readline().strip())

if size == 2:
  print("NO")
  sys.exit(0)

print("YES" if size % 2 == 0 else "NO")