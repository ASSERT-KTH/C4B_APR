word=input()
if(word==word[:1].lower()+word[1:].upper()):
    print(word[:1].upper()+word[1:].lower())
elif(word==word[0:].upper()):
    print(word[0:].lower())
else:
    print(word)