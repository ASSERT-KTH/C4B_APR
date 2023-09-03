word=input()
if(word==word[:1].lower()+word[1:].upper()):
    print(word[:1].upper()+word[1:].lower())
if(word==word[:].upper()):
    print(word[:].lower())
else:
    print(word)