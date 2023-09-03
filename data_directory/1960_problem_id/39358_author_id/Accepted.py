matrix = []
char = '1'
count = 0
i = 0
j = 0
for k in range(0,5):
    
    row = input().split()
    matrix.append(row)
for sub_list in matrix :
    if char in sub_list:
        i = matrix.index(sub_list)
        j = sub_list.index(char)
if i in range(2):
    
    count = 2 - i
else :
    count = i - 2
if j in range(2):
    count = count + (2 - j)
else:
    count = count + (j - 2)
print (count)