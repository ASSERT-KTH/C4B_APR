n=str(input())
t=0
for k in range (len(n)):
    if n[k]=="0":
        t+=1
j=0
for k in range (len(n)):
    if n[k]=="1":
        j+=1
if t>=7 or j>=7:
   print("YES") 
else:
    print("NO")