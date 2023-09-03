import re
s = input().strip()
l = re.split('A|E|I|O|U|Y',s)
print(1+max([len(i) for i in l]))