string = input()

if (len(string) == 1) and string[0].islower():
    print(string.swapcase())
elif (string[0].islower() and string[1:].isupper()) or string.isupper():
    print(string.swapcase())
else:
    print(string)