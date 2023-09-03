s = str(input())
a = s.count('VK')
s.replace('VK', '')
if s.find('VV')!=-1 or s.find('KK')!=-1:
    a += 1
print (a)