s = input()
len_s = len(s)
print(len_s)
t = 'hello'
j = 0
count = 0

for i in t:
    #print('1)',i, s[j], j)
    while True:
        if j == len_s:
            break        
        elif i == s[j]:
            #print('2)',i, s[j], j)
            count += 1
            #print('----',count)
            break
        j += 1
        
        #print(j)
        
        

  
print(count)
if count == 5:
    print('YES')
else:
    print('NO')