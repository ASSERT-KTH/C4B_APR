word = input()

if word.isupper() == True:
    word = word.lower()
elif word[1:].isupper() == True:
    word = word.capitalize()

print(word)