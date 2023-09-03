s =int(input())
numbers = [4,7,47,74,44,77,477,447,474,444,777,747,774,744]
length = len(numbers)
for i in range(0,14):
    if(s%numbers[i]==0):
        print("YES")
        end
print("NO")        
#for i in range(0,14):
    #if(s%numbers[i] !=0):
       # print("NO")
       # break