s=str(input())
while s[0].islower():
    if s[1:len(s)].isupper() or len(s)==1:
        s1= s[0].upper()+s[1:len(s)].lower()
    elif s.isupper():
        s1= s[0].upper()+s[1:len(s)].lower()
    else:
        s1=s
print(s1)
# agf