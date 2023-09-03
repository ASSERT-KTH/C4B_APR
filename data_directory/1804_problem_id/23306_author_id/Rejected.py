n=input("")
cont=0
for k in n:
    if(n.count(k)==1):
        cont+=1
if(2*cont>len(n)):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")