from math import *
a=input().split()
#print(a)
if a[2]=='week':
    if a[0]=='5' or a[0]=='6':
        print(53)
    else:
        print(52)
if a[2]=='month':
    if a[0]=='31':
        print(7)
    elif a[0]=='30':
        print(11)
    else:
        print(12)