word = str(input())

if word.upper() == word:
    print(word.lower())
elif word[1:].upper() == word[1:]:
    for l in word:
        if l.upper() == l:
            print(l.lower(), end='')
        else:
            print(l.upper(), end='')
else:
    print(word)