#problem 825A
size=int(input())
string=input()
list_=list(string)
answer=[]
counter=0
for i in range(0,size):
    if list_[i]=='1':
        counter+=1
    else:
        answer.append(counter)
        counter=0
answer.append(counter)
mystring = ""
for digit in answer:
    mystring += str(digit)
print(mystring)