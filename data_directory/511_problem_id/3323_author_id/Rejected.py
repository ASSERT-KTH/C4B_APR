import sys

input = list(map(int,sys.stdin.readline().strip().split()))

if input[1] == input[0]:
  print("YES")
elif input[2] != 0 and input[1] % input[2] == input[0] % input[2] and input[1] >= input[0]:
  print("YES")
else:
  print("NO")
# 1488581403026