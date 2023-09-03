x = input()
lst = []
i = 0
z = 0
while(i<len(x)):
    if x[i] in lst:
        print(x[i],lst)
        print(i)
        i += 1
        continue
    else:
        lst.append(x[i])
        z += 1
        i += 1
    
if(z%2==0):
    print("CHAT WITH HER!")
elif(z%2==1):
    print("IGNORE HIM!")