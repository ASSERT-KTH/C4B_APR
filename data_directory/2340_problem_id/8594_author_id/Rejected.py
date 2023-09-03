s=input()
s1=s.lower()
s2=s.upper()
set1=set(s)&set(s1)
set2=set(s)&set(s2)
if len(set2)>len(set1):
    print(s2)
else:
    print(s1)