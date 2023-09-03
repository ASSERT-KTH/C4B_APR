n = int(input())
while n % 2 == 0:
  print(n, end=" ")
  n //= 2
for x in range(3, int(n**0.5)+1, 2):
  while n % x == 0:
    print(n, end=" ")
    n //= x
if n != 1:
  print(n, 1)
else:
  print(1)