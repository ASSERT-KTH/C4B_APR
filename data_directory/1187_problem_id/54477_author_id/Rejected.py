text=input()
if text.isupper() or text[:1]==text[:1].lower() and text[1::]==text[1::].upper():
    text=text.lower()
    big =text[:1].upper()
    print (big+text[1::])
else:
    
    print (text)