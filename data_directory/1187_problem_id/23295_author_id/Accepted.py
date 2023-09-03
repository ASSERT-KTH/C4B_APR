s=str(input())
if s[0].islower() and s[1:len(s)].isupper():
    s1= s[0].upper()+s[1:len(s)].lower()
elif s[0].islower() and len(s)==1:
    s1= s[0].upper()+s[1:len(s)].lower()
elif s.isupper():
    s1= s.lower()
else:
    s1=s
print(s1)