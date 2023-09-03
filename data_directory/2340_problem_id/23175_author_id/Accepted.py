s = input()
s = list(s)
count=0
count1=0
for x in s:
    if(x.isupper()):
        count += 1
    elif(x.islower()):
        count1 += 1
s = "".join(s)

if count==count1 or count1>count:
    print(s.lower())
elif count > count1:
    print(s.upper())