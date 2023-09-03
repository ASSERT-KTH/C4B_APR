word = input()
check = False
for i in range(0,len(word)):
    if word[i] =='H' or word[i]=='Q'or word[i] =='9':
        check = True
if check == True :print('YES')
else:print('NO')