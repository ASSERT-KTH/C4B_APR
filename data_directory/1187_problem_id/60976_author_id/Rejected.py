string = input()
if (string[0].islower() and string[1:].isupper()) or string.isupper() or string[0].islower():
    print(string.swapcase())
else:
    print(string)