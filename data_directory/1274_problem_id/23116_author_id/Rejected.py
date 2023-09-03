# http://codeforces.com/problemset/problem/148/A

k = int(input())
l = int(input())
m = int(input())
n = int(input())

d = int(input())

li = []

for i in range(0, d, k):
  li.append(i)


for i in range(0, d, l):
  li.append(i)


for i in range(0, d, m):
  li.append(i)


for i in range(0, d, n):
  li.append(i)


li = set(li)

if k>d or l>d or m>d or n>d:
  print("0")
else:
  print(len(li))