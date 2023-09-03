n = int(input())

if n & 1 :
    print (7, end = '')
    for i in range((n - 3) // 2) :
        print (1, end = '')
else :
    for i in range(n // 2) :
        print (1, end = '')
print ('')