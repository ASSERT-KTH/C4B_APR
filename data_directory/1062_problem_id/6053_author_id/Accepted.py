n = input()
lucky = 0

for x in n :
    if int(x) == 7 :
        lucky += 1
    elif  int(x) == 4:
        lucky += 1

if lucky == 4 :
    print("YES")
elif  lucky ==7 :
    print("YES")
else:
    print("NO")