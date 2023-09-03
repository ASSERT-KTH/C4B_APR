n = int(input())
n += 1
while 1:    
    s = str(n)
    lst = []
    flag = True
    for i in s:
        if i in lst:
            n += 1
            flag = False
        else:
            lst.append(i)
            
    if flag:
        print (n) 
        break
    n += 1