def isDistinct(year) : 

    for i in range(0, 4) : 
        for j in range(0, 4) : 
            if i != j : 
                if year[i] == year[j] :
                    return False
    return True

year = int(input())

for i in range(year + 1, 9000)  :
    if isDistinct(str(i)):
        print(i)
        break