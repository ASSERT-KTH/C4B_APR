#problem 599A
string=input()
list_=string.split()
x=(int(list_[0])+int(list_[1]))*2
y=int(list_[0])+int(list_[1])+int(list_[2])
if x>y:
    print(y)
else:
    print(x)