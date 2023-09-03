word = input()
n = len(word)
b = 'true'
if n != 1:
    for i in range(1, n):
        if word[i].islower():
            b = 'false'
            break
if b == 'true' and word[0].islower():
    word = word[0].upper() + word[1:].lower()
else:
    word = word.lower()
print(word)