from sys import stdin,stdout
inp=input()
stack=[]
string=list(input())
stack.append('z')
count=0;
for i in string:
    if(stack[-1]==i):
        count+=1
    else:
        stack.append(i)
print(count)