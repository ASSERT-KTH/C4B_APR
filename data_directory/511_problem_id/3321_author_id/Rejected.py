import sys
start, value, increment = map(int, sys.stdin.readline().strip().split())

if start == value:
    print ("YES")
    exit()

if increment == 0:
    if value == start:
        print ("YES")
    else:
        print("NO")
    exit()

if start < 0:
    value = value + abs(start)
else:
    value = value - start
start = 0

print(start, value, increment)
#if start == 0:
#
#if value == 0:
#
#
#if value < 0:
#    if increment > 0:
#        if start > 0:
#            print ("NO") 
#        else:
#            if start < value:
#
#            else:
#                print ("NO")
#            
#
#    if increment < 0:
#        if start < 0:
#    
#        else:
#
#if value > 0:
#
#
#
#
#    if (start > 0 and increment > 0) or  (start < 0 and increment > 0:
#        print ("NO")
#        # start is neg and increment is neg
#        
#        
#        print ("YES")
#    else:
#        if  
#
#    else:
#        print ("YES")
#    exit()
#
#if start == 0:
#    if value % increment == 0 and value >= start:
#        print ("YES")
#    else:
#        print ("NO")
#    exit()
#
#
#
#value = value - start
#start = 0

if value % increment == 0 and value >= start:
    print ("YES")
else:
    print ("NO")
# 1488583250099