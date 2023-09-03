s=input()
sU=sL=0
for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        sU+=1
    elif 'a'<=s[i]<='z':
        sL+=1
if sU>sL:
    print(s.upper())
else:
    print(s.lower())