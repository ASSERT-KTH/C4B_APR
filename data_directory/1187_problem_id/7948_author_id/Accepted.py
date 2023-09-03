text = input()
if text[0].islower() and text[1:].isupper():
    print("{0}{1}".format(text[0].upper(), text[1:].lower()))
elif text.isupper():
    print(text.lower())
elif len(text) == 1 and text[0].islower():
    print(text[0].upper())
else:
    print(text)