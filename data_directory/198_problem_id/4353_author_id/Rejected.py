n=bin(int(input()))[:1:-1]
for i in range(len(n)):
 if n[i]=="1":print(i+1,end=" ")