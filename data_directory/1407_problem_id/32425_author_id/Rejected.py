s=input()
a, b=s.split(' ')[0], s.split(' ')[1]
m=max(len(a),len(b))
if len(a)!=m:
    a=(m-len(a))*'0'+a
if len(b)!=m:
    b=(m-len(b))*'0'+b
c=a
a=b
b=c
a=a[::-1]
s=str(int(a)+int(b))
while s.find('0')==0:
    s=s[1:]
print(s)