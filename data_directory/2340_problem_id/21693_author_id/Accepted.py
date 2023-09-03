word=input()
maj=0
mini=0
for i in range(len(word)):
    if(word[i].islower()==True):
        mini=mini+1
    elif(word[i].isupper()==True):
        maj=maj+1
if(maj>mini):
    print(word.upper())
else:
    print(word.lower())