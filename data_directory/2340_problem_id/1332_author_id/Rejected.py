s = input("word :")
a,b=0,0
for c in s:
    if c.isupper():
        a=a+1
    else:
        b=b+1

if a>b:
    print(s.upper())
elif a<b:
    print(s.lower())
else:
    print(s.lower())