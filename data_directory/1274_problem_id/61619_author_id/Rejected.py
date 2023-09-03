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
        if ((i%k == 0) or (i%l == 0) or (i%m == 0) or (i%n == 0)) and (i not in list_drag):
            list_drag.append(i)
            
    print(len(list_drag))