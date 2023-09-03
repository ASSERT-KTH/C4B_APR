# http://codeforces.com/problemset/problem/133/A

s = input()

li = ["H", "Q", "9"]

flag = True

for i in li:
  if i in s:
    print("YES")
    flag = False
    break

if len(s)>1 and s[-1] is "+":
  print("YES")
  flag = False

if flag:
  print("NO")