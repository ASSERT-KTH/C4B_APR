word = input()
count = 0 
output = ''
for x in word:
    if count == 0 and x.islower():
        x = x.upper()
    elif x.isupper():
        x = x.lower()
    else: 
        print (word)
        break
    count += 1
    output += x
if count == len(word):
    print(output)