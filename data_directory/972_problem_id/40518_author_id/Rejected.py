#UWAGA TO JEST ZADaNIE 761A!
from sys import exit
a, b = [int(x) for x in input().split()]
if abs(a-b)>1 or abs(a-b)==0 :
    print("NO")
    exit()
else:
    print("YES")
    exit() #obczaj to