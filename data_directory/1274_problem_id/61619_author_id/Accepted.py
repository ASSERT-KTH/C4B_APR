k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())



if k == 1:
    
    print(d)
    
else:
    
    list_drag = []
    for i in range(1, d+1):
        if i%k == 0:
            list_drag.append(i)
        
        if i%l == 0:
            list_drag.append(i)
            
        if i%m == 0:
            list_drag.append(i)
            
        if i%n == 0:
            list_drag.append(i)
    
    a = set(list_drag)
    
    print(len(a))