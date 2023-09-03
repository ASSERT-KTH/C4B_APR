# -*- coding: utf-8 -*-
def isLatin(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

w = input('Enter a word: ')

while ((len(w) < 1) or (len(w) > 101)) or (w.isalpha() is not True) or (isLatin(w) is False):
    w = input('Enter a non-blank word of Latin letters only: ')

if (w.isupper() is False) and (len(w) is 1):
    w = w.capitalize()
elif (w[1:].isupper() is True) and (w[0].isupper() is False):
    w = w.capitalize()
elif w.isupper() is True:
    w = w.lower()

print(w)