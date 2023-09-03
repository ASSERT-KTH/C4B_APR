l = list(input())

if ((l.count('4')+l.count('7'))!=0) and ((l.count('4')+l.count('7'))%4==0 or (l.count('4')+l.count('7'))%7==0) :
    print('YES')
else:
    print("NO")