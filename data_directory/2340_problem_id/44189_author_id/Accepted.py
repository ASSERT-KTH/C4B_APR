word=input()
capital =0
small=0
for i in range(len(word)):
    if word[i].isupper():
        capital+=1
    else:
        small +=1
if capital>small:
    print(word.upper())
else:
    print(word.lower())