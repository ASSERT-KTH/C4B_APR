import re
new=input()
lower=new.lower()
wovels="aeiou"
res=""
for char in wovels:
 lower=re.sub(char,"",lower)
for char in lower:
 res+="."+char
print(res)