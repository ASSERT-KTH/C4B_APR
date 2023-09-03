word = input()
i = 0
z = 0
while(i<len(word)):
    y = word[i].lower()
    if(y != 'a' and y != 'e' and y != 'y' and y != 'u' and y != 'i' and y != 'o'):
        print("." + word[i].lower(),end="")
    i += 1