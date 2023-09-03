import sys

def isLucky(n):
    for i in n:
        if i != '4' and i!='7':
            return False
    return True

a = str(input())

drap = False

if isLucky(a) and isLucky(str(len(a))) :
    print("YES")
else:
    print("NO")