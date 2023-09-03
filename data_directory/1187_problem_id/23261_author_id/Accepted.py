text = input()

if text.isupper():
    print(text.lower())
elif text[0].islower() and text[1:].isupper():
    print(text[0].upper() + text[1:].lower())
elif len(text) == 1:
    if text.isupper():
        print(text.lower())
    else:
        print(text.upper())
else:
    print(text)