text = input()
bar = 0
baz = 0
if text.isupper():
    print(text.lower())
if text[0].islower() and text[1:].isupper():
    print(text[0].upper() + text[1:].lower())
else:
    print(text)