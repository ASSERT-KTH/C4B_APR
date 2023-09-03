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
ii = i
if i in range(2):
    
    while i < 2:
        matrix[i],matrix[i+1] = matrix[i+1],matrix[i]
        count = count + 1
        i = i + 1    
else :
    while i > 2:
        matrix[i],matrix[i-1] = matrix[i-1],matrix[i]
        count = count + 1
        i = i - 1
matrix_row = matrix.pop(ii)        
if j in range(2):
    
    while j < 2:
        matrix_row[ii],matrix_row[ii+1] = matrix_row[ii+1],matrix_row[ii]
        count = count + 1
        j = j + 1
    
else :
    while j > 2:
        matrix_row[ii],matrix_row[ii-1] = matrix_row[ii-1],matrix[ii]
        count = count + 1
        j = j - 1
print(count)