s = input()
a = ['H', 'Q', '9', '+']

i = 0

while (i <  len(s)):
    if (s[i] in a):
        message = 'YES'
        break
    else:
        message = 'NO'
    i += 1

print(message)