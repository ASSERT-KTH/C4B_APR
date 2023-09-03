s = input()
result=""
for x in s:
    if x in "HQ9+":
        print ("YES")
    else:
        result+=x
print ("NO")