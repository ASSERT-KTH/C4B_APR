s=input()
a, b=s.split(' ')[0], s.split(' ')[1]
print(int(a)+int(b[::-1]))