#Codeforces Beta Round #95
#cAPS lOCK

word  = input()
flag = 0
first = False
if word[0].islower():
        first = True

    
for i in range(1,len(word)):
    if not(word[i].islower()):
        flag = 1
    else:
        flag = 0
        break
if len(word)==1:
  word = word.upper()
  print(word)
    
elif flag and first==False:
    word = word.lower()
    print(word)
elif flag and first==True:
    word = word[0].upper()+word[1:len(word)].lower()
    print(word)
else:
    print(word)