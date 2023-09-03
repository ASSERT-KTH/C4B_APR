import re
char=str(input())
cmd=["H","Q","9"]
time=0
for c in cmd:
 if c in char:
  time+=1
if time>0:
 print("YES")
else:
 print("NO")