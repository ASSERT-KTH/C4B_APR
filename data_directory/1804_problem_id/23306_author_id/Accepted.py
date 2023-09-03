T=input("")
a=len(set(T))
strq=""
for k in T:
    if(not k in T):
        strq+=k
if(a%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")